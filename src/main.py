from validation import Name_Validation,OS_Validation,CPU_Validation,GPU_Validation,RAM_Validation,Disk_Validation,IP_Validation

VMs = []  # Store multiple VM configurations in a List.
count = 0

while True:
    answer = input("\nDo you want to create a New VMachine ? ( Yes / No ) : ").strip().lower()

    if answer == "yes":
        VM_info = {}  # Store single VM in a dictionary.

        print("\nPlease enter the next details of a new VMachine :")

        Name = Name_Validation(input("\nEnter a valid VM name in the format : [ VM name - number]: ").strip())
        OS = OS_Validation(input("Choose an Operating-System : ( Windows, Linux, Mac ) : ").strip().lower())
        CPU = CPU_Validation(input("Enter the number of cores of the CPU ( 1 - 64 ) : "))
        GPU = GPU_Validation(input("Choose GPU vendor ( Nvidia, AMD, Intel ) :  ")).strip().lower()
        RAM = RAM_Validation(input("Enter RAM Memory ( 0 - 256 )GB :  "))
        Disk = Disk_Validation(input("Enter Disk Storage ( 0 - 500 )GB : "))
        IP = IP_Validation(input("Enter an IP Adress ( 0-255.0-255.0-255.0-255 ) : "))


        
        VM_info["Name"] = Name
        VM_info["OS"] = OS
        VM_info["CPU"] = CPU
        VM_info["GPU"] = GPU
        VM_info["RAM"] = RAM
        VM_info["Disk"] = Disk
        VM_info["IP"] = IP

        count =+ 1
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

            