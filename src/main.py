from validation import Name_Validation,OS_Validation,CPU_Validation,GPU_Validation,RAM_Validation,Disk_Validation,IP_Validation

from machine import Machine


VMs = []  # Store multiple VM configurations in a List.
count = 0

while True:
    answer = input("\nDo you want to create a New VMachine ? ( Yes / No ) : ").strip().lower()

    if answer == "yes":
        #VM_info = {}  # Store single VM in a dictionary.

        print("\nPlease enter the next details of a new VMachine :")

        Name = Name_Validation(input("\nEnter a valid VM name in the format : [ VM name - number]: ").strip())
        OS = OS_Validation(input("Choose an Operating-System : ( Windows, Linux, Mac ) : ").strip())
        CPU = CPU_Validation(input("Enter the number of cores of the CPU ( 1 - 64 ) : "))
        GPU = GPU_Validation(input("Choose GPU vendor ( Nvidia, AMD, Intel ) :  ").strip())
        RAM = RAM_Validation(input("Enter RAM Memory in GB (0 - 256) :  ").strip())
        Disk = Disk_Validation(input("Enter Disk Storage in GB (0 - 500) : ").strip())
        IP = IP_Validation(input("Enter an IP Adress ( 0-255.0-255.0-255.0-255 ) : ").strip())


        vm = Machine(Name,OS,CPU,GPU,RAM,Disk,IP)

        #Conversion from Machine Class to Dictionary.
        vm_dict = vm.to_dict()    # Dictionary Conversion for Machine: You’re trying to convert the Machine object into a dictionary using dict(vm), 
                                  # but this might not work because vm is an instance of Machine, 
                                  # and the dict() function expects the object to have a __dict__ method or an iterable that returns key-value pairs. 
                                  # Since you’ve already defined the to_dict() method, you should call vm.to_dict() instead of using dict(vm).

                                  # 'to_dict' is-not mensioned above, because 'Machine' class already contains it.


        # Inserting Data into Dictionary.
        # VM_info["Name"] = Name
        # VM_info["OS"] = OS
        # VM_info["CPU"] = CPU
        # VM_info["GPU"] = GPU
        # VM_info["RAM"] = f"{RAM}GB"
        # VM_info["Disk"] = f"{Disk}GB"
        # VM_info["IP"] = str(IP) # without 'str', an error will accur : 'Object of type IPv4Address is not JSON serializable.'

        count += 1
        VMs.append(vm_dict) # VMs will store the Machine object (not its attributes). 
                            # I want to append a dictionary representation of the object (such as the result of the to_dict() method).



    elif answer == "":
        print("\nNothing was inserted, Please enter 'Yes' or 'No' !")

    else:
        print("\nConfiguration Canceled !")
        break


print(f"\n{count} VMs created !")
print("\nFinal List of Created VMs:")

for i in range(len(VMs)):                     # printing each VM only once with its index.
    print(f"VM num: {i+1} : {VMs[i]}")

# # Saves only if VMs list exists
# if VMs:
#     save_to_json(VMs)  