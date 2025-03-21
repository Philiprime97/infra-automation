from validation import Name_Validation,OS_Validation,CPU_Validation,GPU_Validation,RAM_Validation,Disk_Validation,IP_Validation
import json
import os



CONFIG_FILE = "configs/instances.json"

def save_to_json(data):
    """Save machine data to configs/instances.json."""
    
    # 1. Ensure the 'configs' folder exists
    os.makedirs("configs", exist_ok=True)  
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




VMs = []  # Store multiple VM configurations in a List.
count = 0

while True:
    answer = input("\nDo you want to create a New VMachine ? ( Yes / No ) : ").strip().lower()

    if answer == "yes":
        VM_info = {}  # Store single VM in a dictionary.

        print("\nPlease enter the next details of a new VMachine :")

        Name = Name_Validation(input("\nEnter a valid VM name in the format : [ VM name - number]: ").strip())
        OS = OS_Validation(input("Choose an Operating-System : ( Windows, Linux, Mac ) : ").strip())
        CPU = CPU_Validation(input("Enter the number of cores of the CPU ( 1 - 64 ) : "))
        GPU = GPU_Validation(input("Choose GPU vendor ( Nvidia, AMD, Intel ) :  ").strip())
        RAM = RAM_Validation(input("Enter RAM Memory ( 0 - 256 )GB :  "))
        Disk = Disk_Validation(input("Enter Disk Storage ( 0 - 500 )GB : "))
        IP = IP_Validation(input("Enter an IP Adress ( 0-255.0-255.0-255.0-255 ) : "))


        
        VM_info["Name"] = Name
        VM_info["OS"] = OS
        VM_info["CPU"] = CPU
        VM_info["GPU"] = GPU
        VM_info["RAM"] = f"{RAM}GB"
        VM_info["Disk"] = f"{Disk}GB"
        VM_info["IP"] = str(IP) # with out 'str', an error will accur : 'Object of type IPv4Address is not JSON serializable.'

        count += 1
        VMs.append(VM_info)


        print("\nCreating VMachine...  ")
        print("\nVMachine Details : ")
        print(VM_info)

        # for key,value in VM_info.items():
        #     print(type(f"{key} : {value}"))

        


    elif answer == "":
        print("\nNothing was inserted, Please enter 'Yes' or 'No' !")

    else:
        print("\nConfiguration Canceled !")
        break


print(f"\n{count} VMs created !")
print("\nFinal List of Created VMs:", VMs)

if VMs:
    save_to_json(VMs)
