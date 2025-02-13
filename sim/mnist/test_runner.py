import os
import json
from cocotb_test.simulator import run

def get_src_from_filelist(root_path, model_path):
    n = os.path.join(model_path, "filelist.json")
    with open(n) as filelist:
        files = json.load(filelist)["files"]
    files = [os.path.join(root_path, f) for f in files]
    return files

def get_top_from_filelist(path):
    n = os.path.join(path, "filelist.json")
    with open(n) as filelist:
        top = json.load(filelist)["top"]
    return top


def test_runner():
    MODEL_DIR = os.environ['MODEL_DIR']
    REPO_ROOT = os.environ['REPO_ROOT']
    sources = get_src_from_filelist(REPO_ROOT, MODEL_DIR)
    top = get_top_from_filelist(MODEL_DIR)

    run(
        toplevel=top,
        verilog_sources=sources,
        module="test_mnist",
        sim_build="run",
        timescale="1ns/1ps"
    )

