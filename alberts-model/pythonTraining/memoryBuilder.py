def memoryBuild(CalcsPerSec, BinarySize):
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
    with open("weights1.mem", "w") as f:
        # goes through each matrix in our weights and 
        # seperates them into addressble nbit 1.(n-1) fixed point
        # then chuncks them into addressable sections based on CalcsPerSecond
        for matrix in weights:
            for matrixRow in matrix:
                strsVals = matrixRow.split()
                for i in range(0, len(strsVals), CalcsPerSec):
                    for k in range(i,i+CalcsPerSec):
                        toWrite = float(strsVals[k])  
                        fixed_point_value = int(toWrite * (2**(BinarySize -1)))  # Scale by 2^n for n fractional bits
                        # Convert to signed 8-bit value using two's complement
                        if fixed_point_value < 0:
                            fixed_point_value = (fixed_point_value + (1 << BinarySize)) & 0xFF  
                        f.write(f"{fixed_point_value:0{BinarySize}b}")  # Format as n-bit binary
                    f.write("\n")



    # Write to a Verilog memory file for the biases
    with open("biases1.mem", "w") as f:
        for colVector in biases:
            for strVal in colVector:
                toWrite = float(strVal)  
                fixed_point_value = int(toWrite * (2**(BinarySize -1)))  # Scale by 2^n for n fractional bits
                # Convert to signed n-bit value using two's complement
                if fixed_point_value < 0:
                    fixed_point_value = (fixed_point_value + (1 << BinarySize)) & 0xFF  
                f.write(f"{fixed_point_value:0{BinarySize}b}\n")  # Format as n-bit binary


memoryBuild(784, 8)

