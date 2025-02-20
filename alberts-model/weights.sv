module weights (
    input  logic                  clk_i,
    input  logic           [9:0] rom_addr_i,
    input logic reset_i,
    output logic           [783:0] weight_o
);

    reg [783:0] test_memory [0:9];

    initial begin
        $display("Loading rom for weights.");
        $readmemh("weights.mem", test_memory);
    end

    logic [783:0] row_q, row_d;

    always_ff @(posedge clk_i) begin  
        if(reset_i) begin
            row_q <= 0;
        end else begin
            row_q <= row_d;
        end
    end

  always_comb begin
        row_d = test_memory[rom_addr_i]; 
    end

    assign weight_o = row_q;
endmodule
