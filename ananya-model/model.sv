module model (
    input clk_i,                  // Input clock signal (used to drive the sequential logic)
    input reset_i,                // Input reset signal (resets the internal state)
    
    // Input Interface
    input valid_i,                // Input signal to indicate that input data is valid (for example, when new data is available)
    input [783:0] data_i,         // 784-bit wide input data (each pixel of a flattened 28x28 MNIST image)
    output ready_o,               // Output signal indicating that the model is ready to accept new data
    
    // Output Interface
    output valid_o,               // Output signal indicating that the output data is valid (ready for reading)
    output [3:0] data_o,          // 4-bit output representing the predicted label (0-9) based on the input image
    input ready_i                 // Input signal to indicate that the system is ready to accept output data
);

    // Internal register to hold the input image data (784 bits)
    reg [783:0] data_reg;         // This holds the input data that is being processed
    // Internal register to store the predicted output label (4 bits: one of the digits 0-9)
    reg [3:0] output_data;        // This holds the predicted digit from the model (range: 0 to 9)
    // Register for the valid output signal (indicates if output is valid)
    reg valid_out;                // When set, the output data is valid and can be read

    // The ready_o signal is always high (1) to indicate the model is always ready to receive data
    assign ready_o = 1'b1;        // Model is always ready to accept input data
    
    // The valid_o signal is tied to the valid_out register to show when the output is valid
    assign valid_o = valid_out;   // Output valid signal
    
    // The data_o signal is tied to the output_data register, which holds the predicted label
    assign data_o = output_data;  // Predicted output data (digit 0-9)

    // Always block is triggered on rising edge of clock or reset signal
    always @(posedge clk_i or posedge reset_i) begin
        if (reset_i) begin
            // If reset signal is high, reset all internal registers to initial values
            data_reg <= 784'b0;           // Reset the input data register to 0 (no data)
            output_data <= 4'b0;          // Reset the output data to 0 (predicting digit 0)
            valid_out <= 1'b0;            // Set the output valid signal to low (no valid output)
        end else if (valid_i && ready_o) begin
            // If valid input data is available and the model is ready to accept it
            data_reg <= data_i;          // Store the input data (784 bits) into the data register
            valid_out <= 1'b1;           // Set the valid output signal to high (indicating valid output)
            output_data <= 4'd8;         // Set the output data to 8 (this is just a dummy output for now)
            // In a real implementation, this is where the neural network computation would occur
        end else begin
            // If the input is not valid or the model is not ready, set valid_out to low
            valid_out <= 1'b0;           // Set valid output to low (no valid output at the moment)
        end
    end

endmodule
