from validation import Name_Validation,OS_Validation,CPU_Validation,GPU_Validation,RAM_Validation,Disk_Validation,IP_Validation
from saving_to_json import save_to_json


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
        RAM = RAM_Validation(input("Enter RAM Memory in GB (0 - 256) :  "))
        Disk = Disk_Validation(input("Enter Disk Storage in GB (0 - 500) : "))
        IP = IP_Validation(input("Enter an IP Adress ( 0-255.0-255.0-255.0-255 ) : "))

        VM_info["Name"] = Name
        VM_info["OS"] = OS
        VM_info["CPU"] = CPU
        VM_info["GPU"] = GPU
        VM_info["RAM"] = f"{RAM}GB"
        VM_info["Disk"] = f"{Disk}GB"
        VM_info["IP"] = str(IP) # without 'str', an error will accur : 'Object of type IPv4Address is not JSON serializable.'

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


# Saves only if VMs list exists
if VMs:
    save_to_json(VMs)  