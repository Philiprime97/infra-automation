import json
import os


CONFIG_FILE = "configs/instances.json"

def save_to_json(data):
    """Save machine data to configs/instances.json."""
    
    # 1. Ensure the 'configs' folder exists
    os.makedirs("configs", exist_ok=True)  # exist_ok=True --- checks if 'configs' dir, exists!
	    # "configs" → The name of the folder to create.
        # exist_ok=True → If the folder already exists, don’t throw an error.
    
    # 2. Try to read existing data from the JSON file
    try:
        with open(CONFIG_FILE, "r") as file:
            instances = json.load(file)  # Load existing data
    except (FileNotFoundError, json.JSONDecodeError):
        instances = []  # If file doesn't exist, start with an empty list
    
    # 3. Add new machine data
    instances.extend(data)
    
    # 4. Save updated list back to the file
    with open(CONFIG_FILE, "w") as file:
        json.dump(instances, file, indent=4)  # Pretty-print JSON
    
    print("\nSaving File Procces started...")
    print(f"Saved to {CONFIG_FILE}")
    print("Done !")


