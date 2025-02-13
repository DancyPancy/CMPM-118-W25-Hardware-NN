# Path to repo root
REPO_ROOT ?= $(shell git rev-parse --show-toplevel) 

# Path to bin or executable if added to path
IVERILOG ?= iverilog
VERILATOR ?= verilator

# get the sources holy jank
SIM_SRCS = $(shell python3 $(REPO_ROOT)/utils/get_filelist.py)
SIM_TOP = $(shell python3 $(REPO_ROOT)/utils/get_top.py)

.PHONY: clean lint help

# test hardcoded to use iverilog for now
test: 
	REPO_ROOT=$(REPO_ROOT) SIM=icarus WAVES=1 MODEL_DIR=$(MODEL_DIR) BATCH_SIZE=$(BATCH_SIZE) EPOCHS=$(EPOCHS) \
	 pytest ../sim/$(DATASET)/test_runner.py
	rm -rf $(REPO_ROOT)/sim/$(DATASET)/__pycache__
	rm -rf $(REPO_ROOT)/.pytest_cache
	

# lint runs the Verilator linter on your code
lint:
	verilator --lint-only -top $(SIM_TOP) $(SIM_SRCS) -Wall

# clean sim build
clean:
	rm -rf run

help:
	@echo "  test: simulates with icarus make sure you set your" 
	@echo "        dataset in your Makefile and your files in"
	@echo "        filelist.json"
	@echo "  lint: Run the Verilator linter on all source files"
	@echo "  clean: Remove all compiler outputs."