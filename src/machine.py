from pydantic import BaseModel,Field
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

        # Ensure the 'configs' folder exists
        os.makedirs("configs", exist_ok=True)       # exist_ok=True -> checks if 'configs' dir, exists,if yes,don’t throw an error!
	                                                # "configs" -> The name of the folder to create.
                                                    
    
        # Try to read existing data from the JSON file
        try:
            with open(CONFIG_FILE, "r") as file:
                content = json.load(file)           # Load existing data
        except (FileNotFoundError, json.JSONDecodeError):
            content = []                            # If file doesn't exist, start with an empty list
    
        # Add new machine data
        content.extend(data)                        #extand - means adding each element from data to content at the end of the list.
    
        # 4. Save updated list back to the file
        try:
            with open(CONFIG_FILE, "w") as file:
                json.dump(content, file, indent=4)  # Pretty-print JSON & writes the JSON representation of content directly to file.


                logging.info(f"Data successfully saved to {CONFIG_FILE}")
                print("\nVM configured successfully")
                print(f"VM configuration saved successfully to {CONFIG_FILE}")
                print("Done!")

        except Exception as e:
                logging.error(f"Error saving to {CONFIG_FILE}: {e}")
                print("Error saving the file.")



# Creating VMachine class 
class VMachine(BaseModel):

    # pydantic validation included
    Name : str = Field(...,pattern = r'^[a-zA-Z0-9-_]+$',description ="Name format must be : [ VM name - number]")
    OS : str = Field(...,pattern=r'^(Windows|Linux|Mac)$', description = "Operating-System must be : ( Windows, Linux, Mac )")
    CPU : int = Field(...,ge=1,le=64,description="CPU must be between : 1 - 64")
    GPU : str = Field(...,pattern=r'^(Nvidia|AMD|Intel)$',description = " GPU must be : ( Nvidia, AMD, Intel )")
    RAM : int = Field(...,ge=1,le=256,description="RAM Memory must be (0 - 256)GB")
    Disk : int = Field(...,ge=1,le=500,description="Disk Storage must be (0 - 500)GB)")


    # User input reresented as a dictionary.
    def to_dict(self):               
                return {
                    "Name":self.Name,
                    "OS"  :self.OS,
                    "CPU" :self.CPU,
                    "GPU" :self.GPU,
                    "RAM" :f"{self.RAM}GB",
                    "Disk":f"{self.Disk}GB",
                }



    