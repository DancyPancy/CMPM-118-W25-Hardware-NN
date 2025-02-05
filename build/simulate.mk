
# Path to repo root
REPO_ROOT ?= $(shell git rev-parse --show-toplevel) 

# Path to bin or executable if added to path
IVERILOG ?= iverilog
VERILATOR ?= verilator

.PHONY: clean lint

# test hardcoded to use iverilog for now
test: 
	REPO_ROOT=$(REPO_ROOT) SIM=verilator pytest test_$(DATASET).py -rA

# lint runs the Verilator linter on your code
lint:
	$(VERILATOR) --lint-only -top $(SIM_TOP) $(SIM_SRCS) -Wall

# clean sim build
clean:
	rm -rf run
	rm -rf __pycache__
