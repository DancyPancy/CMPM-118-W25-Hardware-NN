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



    logic [0:783] currentweightsaddy;
	logic [0:7] currentweight;
    weights my_weights (
		.clk_i(clk_i),
    	.rom_addr_i(currentweightsaddy),
    	.weight_o(currentweights)
    );


	// flip flop for data_o
	logic [3:0] data_q, data_d
	always_ff @( posedge clk_i ) begin 
	end


	/* Code */
	always_comb begin 
		

	end
	

endmodule
