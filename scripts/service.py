import subprocess

# Ask for the service name
service = input("\nEnter service name:")

# Run the Bash script and capture the output
result = subprocess.run(["bash", "scripts/service.sh", service ], capture_output=True, text=True)

output = result.stdout.strip()  # Remove extra spaces/newlines

# Check the return code of the Bash script
if result.returncode == 0:
     
    # Clean the output by removing extra spaces and newlines
    output = result.stdout.strip()  # Remove extra spaces/newlines
    print(f"Bash script output:\n{output}")
else:
    # Print the error if the script fails
    print(f"Error: {result.stderr.strip()}")