module biases#() (
    input  logic                  clk_i,
    input  logic           [9:0] rom_addr_i,
    input logic reset_i,
    output logic           [7:0] bias_o
);

    reg [7:0] test_memory [0:9];

    initial begin
        $display("Loading rom for biases.");
        $readmemh("biases.mem", test_memory);
    end

    logic [7:0] bias_q, bias_d;

    always_ff @(posedge clk_i) begin  
        if(reset_i) begin
            bias_q <= 0;
        end else begin
            bias_q <= bias_d;
        end
    end

  always_comb begin
        bias_d = test_memory[rom_addr_i]; 
    end

    assign bias_o = bias_q;
endmodule
