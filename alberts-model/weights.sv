module weights #() (
    input  logic                  clk_i,
    input  logic           [783:0] rom_addr_i,
    output logic           [7:0] weight_o
);

    reg [7:0] test_memory [0:783];
    initial begin
        $display("Loading rom.");
        $readmemh("weights.mem", weights_memory);
    end

   logic [7:0] weight_q
   always_ff @( posedge clk_i ) begin  
        weight_q=weights_memory[rom_addr_i];
   end

   assign weight_o = weight_q;
endmodule