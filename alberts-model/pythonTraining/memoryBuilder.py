# Load weights from the text file
weight_file = "model_weights.txt"
with open(weight_file, "r") as f:
    lines = f.readlines()


#Slipt the text file into a arrays for the biases and weights for each layer
startofWeightsAndBias=[]
for index, line in enumerate(lines):
    if("weight" in line):
        startofWeightsAndBias.append(index)
    if("bias" in line):
        startofWeightsAndBias.append(index)

weights=[]
for i in range(0, len(startofWeightsAndBias), 2):
    weights.append(lines[startofWeightsAndBias[i]+1:startofWeightsAndBias[i+1]-1])


biases=[]
for i in range(1,len(startofWeightsAndBias)-1,2):
    biases.append(lines[startofWeightsAndBias[i]+1:startofWeightsAndBias[i+1]-1])
biases.append(lines[startofWeightsAndBias[-1]+1:-1])


# Write to a Verilog memory file for the weights
with open("weights.mem", "w") as f:
    for matrix in weights:
        for matrixRow in matrix:
            strsVals = matrixRow.split()
            for strVal in strsVals:
                toWrite = float(strVal)  
                #idk how to fixed point but its 1.7 scaling and this what GPT gave me
                fixed_point_value = int(toWrite * (2**7))  # Scale by 2^7 for 7 fractional bits
                # Convert to signed 8-bit value using two's complement
                if fixed_point_value < 0:
                    fixed_point_value = (fixed_point_value + (1 << 8)) & 0xFF  
                f.write(f"{fixed_point_value:08b}")  # Format as 8-bit binary
            f.write("\n")




# Write to a Verilog memory file for the biases
with open("biases.mem", "w") as f:
    for colVector in biases:
        for strVal in colVector:
            toWrite = float(strVal)  
            #idk how to fixed point but its 1.7 scaling and this what GPT gave me
            fixed_point_value = int(toWrite * (2**7))  # Scale by 2^7 for 7 fractional bits
            # Convert to signed 8-bit value using two's complement
            if fixed_point_value < 0:
                fixed_point_value = (fixed_point_value + (1 << 8)) & 0xFF  
            f.write(f"{fixed_point_value:08b}\n")  # Format as 8-bit binary

