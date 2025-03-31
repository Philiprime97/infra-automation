from pydantic import BaseModel,Field,IPvAnyAddress,ValidationError
import logging
import json
import os


# Log format:
logging.basicConfig(
            filename="logs/provisioning.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s", 
            )

# Saving to JSON file:
def save_to_json(data):
        
        CONFIG_FILE = "configs/instances.json"

        # 1. Ensure the 'configs' folder exists
        os.makedirs("configs", exist_ok=True)       # exist_ok=True --- checks if 'configs' dir, exists!
	                                                # "configs" → The name of the folder to create.
                                                    # exist_ok=True → If the folder already exists, don’t throw an error.
    
        # 2. Try to read existing data from the JSON file
        try:
            with open(CONFIG_FILE, "r") as file:
                content = json.load(file)           # Load existing data
        except (FileNotFoundError, json.JSONDecodeError):
            content = []                            # If file doesn't exist, start with an empty list
    
        # 3. Add new machine data
        content.extend(data)                        #extand - means adding each element from data to content at the end of the list.
    
        # 4. Save updated list back to the file
        try:
            with open(CONFIG_FILE, "w") as file:
                json.dump(content, file, indent=4)  # Pretty-print JSON
                logging.info(f"Data successfully saved to {CONFIG_FILE}")
                print("\nVM configured successfully")
                print(f"VM configuration saved successfully to {CONFIG_FILE}")
                print("Done!")
        except Exception as e:
                logging.error(f"Error saving to {CONFIG_FILE}: {e}")
                print("Error saving the file.")


# Pydantic serves both as a class definition and a validation framework at the same time!

class VMachine(BaseModel):

    Name : str = Field(...,pattern = r'^[a-zA-Z0-9-_]+$',description ="Name format must be : [ VM name - number]")
    OS : str = Field(...,pattern=r'^(Windows|Linux|Mac)$', description = "Operating-System must be : ( Windows, Linux, Mac )")
    CPU : int = Field(...,ge=1,le=64,description="CPU must be between : 1 - 64")
    GPU : str = Field(...,pattern=r'^(Nvidia|AMD|Intel)$',description = " GPU must be : ( Nvidia, AMD, Intel )")
    RAM : int = Field(...,ge=1,le=256,description="RAM Memory must be (0 - 256)GB")
    Disk : int = Field(...,ge=1,le=500,description="Disk Storage must be (0 - 500)GB)")
    IP : IPvAnyAddress 


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

# In Pydantic v2, the regex parameter has been replaced by the 'pattern' parameter in the Field() function.

# def get_vm_input():
        
#     try:       
#         #  Collect user input
#         Name = input("\nEnter a valid VM name in the format : [ VM name - number]: ").strip()
#         OS = input("Choose an Operating-System : ( Windows, Linux, Mac ) : ").strip()
#         CPU = int(input("Enter the number of cores of the CPU ( 1 - 64 ) : "))
#         GPU = input("Choose GPU vendor ( Nvidia, AMD, Intel ) :  ").strip()
#         RAM = int(input("Enter RAM Memory in GB (0 - 256) :  "))
#         Disk = int(input("Enter Disk Storage in GB (0 - 500) : "))
#         IP = input("Enter an IP Adress ( 0-255.0-255.0-255.0-255 ) : ")  # i removed 'int' because pydantuc handles with string automatically.

#         # Validate the inputs using pydantic via the VMachine class
#         vm = VMachine(Name=Name,OS=OS,CPU=CPU,GPU=GPU,RAM=RAM,Disk=Disk,IP=IP)

#         logging.info(f"VMachine Created : {vm.to_dict()}")  # every time a single machine is created, it has a record log.
#         save_to_json([vm.to_dict()])                        # every time a single machine is created, it is saved in json and stored in instances.json.
#                                                             # I dont need to wait every time i press 'no', so a machine will be loged and saved, it is now doing it immediatly, when a class is being called.
#         return vm


#     except ValidationError as e:
#         logging.error(f"Validation error(s) occurred: {e}")
#         print(f"\nValidation Error(s):")
#         for error in e.errors():
#             print(f"- {error['loc']}: {error['msg']}")

    