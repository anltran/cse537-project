import subprocess

path = r'UkeireCalculator\index.js'
hand = "1m1m5m7m9m1p2p3p4p5p8p3z5z6z"

# Command to execute
command = ["node", path, hand, "1"]

# Execute the command and capture the output
result = subprocess.run(command, capture_output=True, text=True, check=True)

# Access the output and error streams
output = result.stdout
error = result.stderr

# Print the output and error
# print("Output:", output)
# print("Error:", error)

print(output)