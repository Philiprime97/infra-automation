from machine import VMachine,logging,save_to_json
from pydantic import ValidationError
from scripts.main_service import install_service

# I added the __init__.py file because it is a special Python file used to mark a directory as a package.
# It allows Python to recognize the folder as a module that can be imported.

def main():

    VMs = []  # Store created VM configurations in a List, VMs is used for the terminal to be friendly and readable. 
    count = 0 # Counts the number of VMs created.

    # Makes the log to be more user-friendly
    logging.info("-" * 100)
    logging.info("==== Session Started ====")
    logging.info("-" * 100)
    logging.info("User chose to create a new VMachine.")


    while True:
        # Asks the user for input 'Yes' or 'No'
        answer = input("\nDo you want to create a New VMachine ? ( Yes / No ) : ").strip().lower()

        if answer == "yes":

            # Asks the user to enter the VMachine details
            print("\nPlease enter the next details of a new VMachine :")
            
            try:
                # Collect user input directly
                Name = input("\nEnter a valid VM name (ex: VM-1): ").strip()
                OS = input("Choose an Operating System (Windows, Linux, Mac): ").strip()
                CPU = int(input("Enter CPU cores (1-64): "))
                GPU = input("Choose GPU vendor (Nvidia, AMD, Intel): ").strip()
                RAM = int(input("Enter RAM size in GB (1-256): "))
                Disk = int(input("Enter Disk size in GB (1-500): "))

                # Creating a vm instance of a VMachine class from machine.py file
                vm = VMachine(Name=Name, OS=OS, CPU=CPU, GPU=GPU, RAM=RAM, Disk=Disk)

                # Saves to JSON immediately
                save_to_json([vm.to_dict()])

                # installing service on vm
                install_service(vm)   

                VMs.append(vm)  # Adds the vm that is created to the VMs list.
                count += 1       
                logging.info(f"VM #{count} created: {vm.to_dict()}")

            
            except ValidationError as e:
                logging.error(f"Validation error(s) occurred: {e}")
                print(f"\nValidation Error(s):")
                for error in e.errors():                                # 'e.errors()' is a list of dictionaries, where each dictionary contains details about a validation error.
                    print(f"- {error['loc']}: {error['msg']}")          # 'error' in 'e.errors()' is a dictionary with keys, 
                                                                        # where 'loc' indicates of location and 'msg' indicates a message of the error
                                                                        # error['loc'] : prints which field had an issue
                                                                        # error['msg'] : describes the issue

            except Exception as e:
                logging.error(f"Error creating VM: {e}")
                print(f"\nError: {e}")

            


        elif answer == "":
            logging.warning("No input received, user prompted again.")
            print("\nNothing was inserted, Please enter 'Yes' or 'No' !")

        else:
            logging.info("Configuration canceled by user.")
            print("\nConfiguration Canceled !")
            break

     
    # Makes the log to be more user-friendly       
    logging.info(f"{count} VMs created.")
    logging.info("-" * 100)
    logging.info("===== Session Ended =====")
    logging.info("-" * 100)
    

    # Printing only on the terminal to sum up
    print(f"\n{count} VM(s) created !\n")
    if count > 0:
        print("\nFinal List of Created VM(s):")       
        for i in range(len(VMs)):                     # Iterate over the the number of vms created in the list of VMs 
            print(f"VM No: {i+1} : {VMs[i]}\n")       # Printing the object VM[i] at its index i 
    else:
        print(" No VM(s) were created! ")



# Calling for the script to run directly
if __name__ == "__main__":
    main()