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

	Goals
	have a counter that sets does current row, put it in a flipflop
	once row is final set valid to high
	Ready Valid -> 


    logic [9:0] outVector_d, outVector_q
	logic [4:0] curRow_d, curRow_q
    always_ff @(posedge clk_i) begin  
        if(reset_i || !valid_i || !ready_i) begin
			outVector_q <= 0;
			curRow_q <= 0;
        end else begin
			outVector_q <= outVector_d;
			curRow_q <= curRow_d;
        end
    end

	always_comb begin
		curRow_d = curRow_q
		outVector_d
	end
	




	

endmodule
