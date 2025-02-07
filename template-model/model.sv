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

	/* Code */

	assign ready_o = 1'b1;
	assign valid_o = 1'b1;
	assign data_o = 4'd8;

endmodule
