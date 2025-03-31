from machine import VMachine,logging,save_to_json
from scripts.service import install_service

def main():

    VMs = []  # Store created VM configurations in a List, VMs is used for the terminal to be friendly and readable. 
    count = 0 # Number of VMs created.

    while True:
        answer = input("\nDo you want to create a New VMachine ? ( Yes / No ) : ").strip().lower()

        if answer == "yes":


            logging.info("-" * 100)
            logging.info("==== Session Started ====")
            logging.info("-" * 100)
            logging.info("User chose to create a new VMachine.")
            print("\nPlease enter the next details of a new VMachine :")
            
            
            #data = get_vm_input() # Calling fot function to create vm, this function getting user input
            
            try:
                # Collect user input directly
                Name = input("\nEnter a valid VM name (ex: VM-1): ").strip()
                OS = input("Choose an Operating System (Windows, Linux, Mac): ").strip()
                CPU = int(input("Enter CPU cores (1-64): "))
                GPU = input("Choose GPU vendor (Nvidia, AMD, Intel): ").strip()
                RAM = int(input("Enter RAM size in GB (1-256): "))
                Disk = int(input("Enter Disk size in GB (1-500): "))
                IP = input("Enter an IP Address (e.g., 192.168.1.1): ").strip()

                # Creating a vm instance of a VMachine class 
                vm = VMachine(Name=Name, OS=OS, CPU=CPU, GPU=GPU, RAM=RAM, Disk=Disk, IP=IP)

                # Save to JSON immediately
                save_to_json([vm.to_dict()])
                #print("\nVM configured and saved successfully!")

                install_service(vm)   # installing service on vm


                # Store and log the VM instance
                VMs.append(vm)  # Store the VMachine object, not just its dictionary
                count += 1
                logging.info(f"VM #{count} created: {vm.to_dict()}")

            except Exception as e:
                logging.error(f"Error creating VM: {e}")
                print(f"\nError: {e}")

            # if data:
            #     count += 1
            #     #VMs.append(data)  # Store the dictionary representation of the VM, VMs will store the Machine object (not its attributes). 
            #     logging.info(f"VM #{count} created with details: {data}")



        elif answer == "":
            logging.warning("No input received, user prompted again.")
            print("\nNothing was inserted, Please enter 'Yes' or 'No' !")

        else:
            logging.info("Configuration canceled by user.")
            print("\nConfiguration Canceled !")
            break

     

    logging.info(f"{count} VMs created.")
    logging.info("-" * 100)
    logging.info("===== Session Ended =====")
    logging.info("-" * 100)
    

    print(f"\n{count} VM(s) created !\n")
    if count > 0:
        print("\nFinal List of Created VM(s):")       # printing only for the terminal,to sum up,thats why i used VMs as list!
        for i in range(len(VMs)):                     # printing each VM only with its index.
            print(f"VM No: {i+1} : {VMs[i]}\n")
    else:
        None




if __name__ == "__main__":
    main()