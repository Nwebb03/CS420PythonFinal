import subprocess

# Specify the full path to the MATLAB executable
# Adjust the path accordingly
matlab_executable = '/Applications/MATLAB_R2023b.app/bin/matlab'
# Load the matlab code
with open('matlabcode1.m', 'r') as file:
    matlabcode = file.read()
# Set up MATLAB environment
Matlab_process = subprocess.Popen([matlab_executable, '-nodisplay', '-nosplash', '-nodesktop'],
stdin=subprocess.PIPE, text=True)
# Send MATLAB script to the MATLAB process
Matlab_process.communicate(input=matlabcode)

# Read values from 'data.txt'
with open('input.txt', 'r') as file:
    line = file.readline()
    input_array = [int(value) for value in line.split()]
# Compile the C program (assuming it's saved as CProg.c)
subprocess.run(["gcc", "CProg.c", "-o", "CProg"])
# Run the compiled C program with the input array as arguments
input_array_str = [str(value) for value in input_array]
process = subprocess.run(["./CProg"] + input_array_str, capture_output=True, text=True)
# Store the output of the C program in a Python variable
output_variable = process.stdout.strip()


with open('c_output.txt', 'w') as f:
    f.write(output_variable)

subprocess.run(["ghc", "HaskellProg.hs", "-o", "HaskellProg"])
# Run the compiled haskell program with the input array as arguments
process = subprocess.run(["./HaskellProg"] + input_array_str, capture_output=True, text=True)
# Store the output of the haskell program in a Python variable
output_variable = process.stdout.strip()

with open('Haskell_output.txt', 'w') as f:
    f.write(output_variable)

#Do the same thing but with prolog
prolog_input = "[" + ",".join(map(str, input_array)) + "]."

result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'PrologProg.pl'], input=prolog_input,
capture_output=True, text=True)
#Take the output from prolog and save it in a variable
result = result.stdout.strip()
#Write output to a new file
with open('Prolog_output.txt', 'w') as f:
    f.write(result)


with open('matlabcode2.m', 'r') as file2:
    matlabcode2 = file2.read()
# Set up MATLAB environment
Matlab_process2 = subprocess.Popen([matlab_executable],
stdin=subprocess.PIPE, text=True)
# Send MATLAB script to the MATLAB process
Matlab_process2.communicate(input=matlabcode2)