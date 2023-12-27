import subprocess
# Your input array
input_array = ["1", "2", "3", "4", "5"]
# Compile the C program (assuming it's saved as CProg.c)
subprocess.run(["gcc", "CProg.c", "-o", "CProg"])
# Run the compiled C program with the input array as arguments
process = subprocess.run(["./CProg"] + input_array, capture_output=True, text=True)
# Store the output of the C program in a Python variable
output_variable = process.stdout.strip()
# Print or use the stored output
print("C program output:")
print(output_variable)

input_array = ["1", "2", "3", "4", "5"]
# Compile the haskell program
subprocess.run(["ghc", "HaskellProg.hs", "-o", "HaskellProg"])
# Run the compiled haskell program with the input array as arguments
process = subprocess.run(["./HaskellProg"] + input_array, capture_output=True, text=True)
# Store the output of the haskell program in a Python variable
output_variable = process.stdout.strip()
# Print or use the stored output
print("Haskell program output:")
print(output_variable)

prolog_input = "[" + ",".join(map(str, input_array)) + "]."

result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'PrologProg.pl'], input=prolog_input,
capture_output=True, text=True)

result = result.stdout.strip()

print("Prolog output: \n",result)
