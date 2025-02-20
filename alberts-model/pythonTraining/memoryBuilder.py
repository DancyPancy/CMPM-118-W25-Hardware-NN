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






# Write to a Verilog memory file
# with open("weights.mem", "w") as f:
#     for w in fixed_point_weights:
#         f.write(f"{w:016b}\n")  # 16-bit binary format
