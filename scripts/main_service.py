from src.machine import logging
import subprocess


# A function of installing a service
def install_service(vm):
    
    # Service is given
    service = "google"
    logging.info(f"{service} is asked to be installed")


    # Checks if a service exists
    if service:
        print(f"\nInstalling '{service}' on VM: {vm.Name}...")

        # Runs the Bash script and captures it's output
        result = subprocess.run(["bash", "scripts/service.sh", service], capture_output=True, text=True)
        logging.info(f"{service} is installing")

        # Checks the exit-code of the Bash script
        if result.returncode == 0:
            print(f"\nService installed successfully on {vm.Name}:")
            logging.info(f"{service} done installing")
            print(result.stdout.strip())  # Prints the script output
        else:
            print(f"\nError installing service on {vm.Name}: {result.stderr.strip()}")
            logging.error(f"{service} was not installed")
    else:
        return " No service was entered "