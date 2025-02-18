# Load weights from the text file
weight_file = "model_weights.txt"
with open(weight_file, "r") as f:
    lines = f.readlines()

toprint=[]
for line in lines:
    if(len(line)>75):
        values = line.strip().split()
        toprint.append(values)


fixed_point_weights = []
for strvalue in values:
    value = float(strvalue)
    float_val = min(1.0, max(-1.0, value))
    # Scale the float value by 2^7 (127)
    fixed_point = int(round(float_val * 127))
    # Handle negative numbers (two's complement)
    if fixed_point < 0:
        fixed_point = (1 << 8) + fixed_point
        
    fixed_point_weights.append(fixed_point & 0xFF)






# Write to a Verilog memory file
with open("weights.mem", "w") as f:
    for w in fixed_point_weights:
        f.write(f"{w:016b}\n")  # 16-bit binary format
