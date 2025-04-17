import subprocess

path = r'C:\Users\trana\Desktop\cse537-project\ShantenCalculator\ShantenCalculator\bin\Debug\net6.0\ShantenCalculator.exe'
hand = "1499m38p1258s222z"

# Command to execute
command = [path, hand]

# Execute the command and capture the output
result = subprocess.run(command, capture_output=True, text=True, check=True)

# Access the output and error streams
output = result.stdout
error = result.stderr

# Print the output and error
# print("Output:", output)
# print("Error:", error)

print(output)