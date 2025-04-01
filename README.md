# infra-automation
DevOps Project


DevOps Infrastructure Provisioning & Configuration Automation

Overview

This project aims to create a modular Python-based tool to simulate infrastructure provisioning and service configuration. As the project evolves, future iterations will integrate AWS and Terraform for real infrastructure deployment. For now, provisioning is simulated to demonstrate automation principles.

Objectives

1. Accept and validate user inputs for defining virtual machines (VMs).
2. Implement a modular architecture using Python classes.
3. Automate service installation using Bash scripts.
4. Implement logging and error handling for robustness.

Project Structure:

infra-automation/
|-- scripts/      # Bash scripts for service installation
|-- configs/      # JSON configuration files
|-- logs/         # Log files
|-- src/          # Python source code
|-- README.md     # Documentation



Setup & Installation

1. Clone the Repository
git clone [<repository_url>](https://github.com/Philiprime97/infra-automation.git)
cd infra-automation

2. Set Up a Virtual Environment
python -m venv my_venv1
source my_venv1/bin/activate  # macOS/Linux

3. Install Dependencies
pip install -r requirements.txt




Features & Implementation

1. User Input & Validation
Users define VM configurations interactively.
Validation ensures correct input format.
Configurations are stored in configs/instances.json.

2. Modular Python Code
Machine class (src/machine.py) handles VM properties.
The class provides structured data output and logging.
The main script (infra_simulator.py) interacts with the class.

3. Automating Service Installation
A Bash script installs a basic service (e.g., Nginx).
Python’s subprocess module executes the script.
Error handling ensures smooth execution.

4. Logging & Error Handling
Logs are saved in logs/provisioning.log.
Captures provisioning status, errors, and success messages.



Usage

Run the simulation:
python infra_simulator.py

Expected Output:
instances.json: Contains VM details.

provisioning.log: Logs the process flow.
Service Installed: If applicable.


- Project Done !