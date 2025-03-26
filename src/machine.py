import logging
import json
import os


logging.basicConfig(
            filename="logs/machine.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s", 
            )


def save_to_json(data):
        """Save machine data to configs/instances.json."""

        CONFIG_FILE = "configs/instances.json"

        # 1. Ensure the 'configs' folder exists
        os.makedirs("configs", exist_ok=True)  # exist_ok=True --- checks if 'configs' dir, exists!
	        # "configs" → The name of the folder to create.
            # exist_ok=True → If the folder already exists, don’t throw an error.
    
        # 2. Try to read existing data from the JSON file
        try:
            with open(CONFIG_FILE, "r") as file:
                content = json.load(file)  # Load existing data
        except (FileNotFoundError, json.JSONDecodeError):
            content = []  # If file doesn't exist, start with an empty list
    
        # 3. Add new machine data
        content.extend(data)
    
        # 4. Save updated list back to the file
        try:
            with open(CONFIG_FILE, "w") as file:
                json.dump(content, file, indent=4)  # Pretty-print JSON
                logging.info(f"Data successfully saved to {CONFIG_FILE}")
                print("\nSaving VMachine configuration...")
                print(f"Saved to {CONFIG_FILE}")
                print("Done!")
        except Exception as e:
                logging.error(f"Error saving to {CONFIG_FILE}: {e}")
                print("Error saving the file.")


class VM():
    def __init__(self,Name,OS,CPU,GPU,RAM,Disk,IP):
        self.Name = Name
        self.OS   = OS
        self.CPU  = CPU
        self.GPU  = GPU
        self.RAM  = RAM
        self.Disk = Disk
        self.IP   = IP

        logging.info(f"VMachine Created : {self.to_dict()}")  # every time a single machine is created, it has a record log.
        save_to_json([self.to_dict()])                       # every time a single machine is created, it is saved in json and stored in instances.json.
                                                             # I dont need to wait every time i press 'no', so a machine will be loged and saved, it is now doing it immediatly, when a class is being called.

        print("\nVMachine Created !  ")
        print("\nVMachine Details : \n")

        for key,value in self.to_dict().items():  # Showing a more readable VM info on the terminal(stdout).
            print(f"{key} : {value}")  



        # Return the Machine details as a dictionary - 'to_dict' converts the object's attributes into a dictionary for easy storage and display
    def to_dict(self):               
        return {
            "Name":self.Name,
            "OS"  :self.OS,
            "CPU" :self.CPU,
            "GPU" :self.GPU,
            "RAM" :f"{self.RAM}GB",
            "Disk":f"{self.Disk}GB",
            "IP"  :str(self.IP)
        }
    

