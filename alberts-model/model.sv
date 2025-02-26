module model
	(input	[0:0]	clk_i
	,input	[0:0]	reset_i

	/* Input Interface */
	,input	[0:0]	valid_i
	,input	[783:0]	data_i
	,output [0:0]	ready_o

	/* Output Interface */
	,output	[0:0]	valid_o
	,output	[3:0]	data_o
	,input	[0:0]	ready_i
	);

    logic [79:0] outVector_d, outVector_q; // len 10 vector with 8 bit representations
	logic [3:0] curRow_d, curRow_q; //represents the current row col multiplication

	logic [7:0] bias;
	biases my_biases (
        .clk_i(clk_i),
        .rom_addr_i(curRow_q),
        .reset_i(reset_i),
		.bias_o(bias)
    );

	logic [783:0] weight;
	weights my_weights (
        .clk_i(clk_i),
        .rom_addr_i(curRow_q),
        .reset_i(reset_i),
		.weight_o(weight)
	);
	

	// Goals
	// have a counter that sets does current row, put it in a flipflop
	// once row is final set valid to high
	// Ready Valid -> 

    always_ff @(posedge clk_i) begin  
        if(reset_i || !valid_i || !ready_i) begin
			outVector_q <= 80'b0;
			curRow_q <= 5'b0;
        end else begin
			outVector_q <= outVector_d;
			curRow_q <= curRow_d;
        end
    end

	always_comb begin
		curRow_d = curRow_q + 1;
		outVector_d = outVector_q;
   		for (int i = 0; i < 98; i++) begin // 784 bits / 8 bits = 98 segments
        	outVector_d = outVector_d + (weight[((8*i) + 7) : (8*i)] * bias);
   		end
	end



endmodule
