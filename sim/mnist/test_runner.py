import os
import json
from cocotb_test.simulator import run

def get_src_from_filelist(path):
    n = os.path.join(path, "filelist.json")
    with open(n) as filelist:
        files = json.load(filelist)["files"]
    files = [os.path.join(path, f) for f in files]
    return files

def get_top_from_filelist(path):
    n = os.path.join(path, "filelist.json")
    with open(n) as filelist:
        top = json.load(filelist)["top"]
    return top


def test_runner():
    MODEL_DIR = os.environ['MODEL_DIR']
    sources = get_src_from_filelist(MODEL_DIR)
    top = get_top_from_filelist(MODEL_DIR)

    run(
        toplevel=top,
        verilog_sources=sources,
        module="test_mnist",
        sim_build="run",
        timescale="1ns/1ps"
    )

