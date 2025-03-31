import subprocess

def install_service1():
    # Ask for the service name
    service = "google"

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

    return output



def install_service(vm):
    """Install a service on the given VM using the Bash script."""
    service = input(f"\nEnter the service name to install on {vm.Name}: ").strip()

    if service:
        print(f"\nInstalling '{service}' on VM: {vm.Name}...")
        result = subprocess.run(["bash", "scripts/service.sh", service], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"\nService installed successfully on {vm.Name}:")
            print(result.stdout.strip())  # Show script output
        else:
            print(f"\nError installing service on {vm.Name}: {result.stderr.strip()}")