# Get repo root if not set already
REPO_ROOT ?= $(shell git rev-parse --show-toplevel)

# Get current directory
MODEL_DIR = $(shell pwd)

# set dateset
DATASET = mnist

# top module name
SIM_TOP = model

# all sim sources including top module
SIM_SRCS = $(MODEL_DIR)/model.sv

-include $(REPO_ROOT)/build/simulate.mk
