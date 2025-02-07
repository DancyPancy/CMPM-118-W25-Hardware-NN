# Path to repo root
REPO_ROOT ?= $(shell git rev-parse --show-toplevel) 

# Path to bin or executable if added to path
IVERILOG ?= iverilog
VERILATOR ?= verilator


.PHONY: clean lint

# test hardcoded to use iverilog for now
test: 
	REPO_ROOT=$(REPO_ROOT) SIM=icarus WAVES=1 MODEL_DIR=$(MODEL_DIR) pytest ../sim/$(DATASET)/test_runner.py
	rm -rf $(REPO_ROOT)/sim/$(DATASET)/__pycache__
	rm -rf $(REPO_ROOT)/.pytest_cache
	

# lint runs the Verilator linter on your code
lint:
	verilator --lint-only -top $(SIM_TOP) $(SIM_SRCS) -Wall

# clean sim build
clean:
	rm -rf run
