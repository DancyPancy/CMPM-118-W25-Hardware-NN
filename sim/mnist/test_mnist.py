import pytest
import os
from pathlib import Path

import cocotb
from cocotb.triggers import FallingEdge, RisingEdge, Timer
from cocotb_test.simulator import run
from cocotb.clock import Clock
from cocotb.binary import BinaryValue
from cocotb.regression import TestFactory


import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


def get_testloader_mnist(batch_size=32):
    transform = transforms.Compose([transforms.ToTensor(), lambda x: x>0])
    dataset = torchvision.datasets.MNIST(root="../../sim/mnist/data", train=False, download=True, transform=transform)
    return DataLoader(dataset, batch_size=batch_size, shuffle=False)

async def input_driver_mnist(dut, images):
    dut.valid_i.value = 0
    for image in images.view(-1, 784):
        await FallingEdge(dut.clk_i)
        dut.data_i.value = BinaryValue(value="".join(str(int(bit)) for bit in image), n_bits=784)
        dut.valid_i.value = 1
        if dut.ready_o != 1:
            await RisingEdge(dut.ready_o)
        await RisingEdge(dut.clk_i)
        dut.valid_i.value = 0


async def output_checker_mnist(dut, labels):
    score = 0
    dut.ready_i.value = 1
    for label in labels:
        if (dut.valid_o.value != 1):
            await RisingEdge(dut.valid_o)
        await RisingEdge(dut.clk_i)
        if (int(label) == dut.data_o.value):
            score += 1
    dut.ready_i.value = 0
    return score

async def reset_gen(dut):
    dut.reset_i.value = 0
    await FallingEdge(dut.clk_i)
    dut.reset_i.value = 1
    await Timer(10, units="ns")
    await FallingEdge(dut.clk_i)
    dut.reset_i.value = 0

async def batch_test_mnist(dut, idx, images, labels):
    dut.reset_i.value = 0
    dut.data_i.value = 0
    dut.valid_i.value = 0
    dut.ready_i.value = 0
    
    cocotb.start_soon(Clock(dut.clk_i, 1, units="ns").start())
    
    await reset_gen(dut)
    
    drive_in = cocotb.start_soon(input_driver_mnist(dut, images))
    check_out = cocotb.start_soon(output_checker_mnist(dut, labels))

    await drive_in
    score = await check_out
    mode = "a" if idx else "w" 
    with open("test_results.txt", mode) as f:
        f.write(f"Batch {idx+1}:\tScore {score}/{labels.shape[0]},\tAccuracy {score/labels.shape[0]*100}%\n")

def generate_batchtests(test_function, test_loader, epochs=16):
    for idx, test_data in enumerate(test_loader):
        if idx >= epochs:
            break
        images, labels = test_data
        tf=TestFactory(test_function)
        tf.add_option(("idx", "images", "labels"), [(idx, images, labels)])
        tf.generate_tests(postfix=str(idx))


batch_size = int(os.environ['BATCH_SIZE'])
epochs = int(os.environ['EPOCHS'])
test_loader = get_testloader_mnist(batch_size)
generate_batchtests(batch_test_mnist, test_loader, epochs)