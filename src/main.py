from machine import get_vm_input,logging

def main():

    VMs = []  # Store multiple VM configurations in a List.
    count = 0 # Number of VMs created.

    while True:
        answer = input("\nDo you want to create a New VMachine ? ( Yes / No ) : ").strip().lower()

        if answer == "yes":


            logging.info("-" * 100)
            logging.info("==== Session Started ====")
            logging.info("User chose to create a new VMachine.")
            print("\nPlease enter the next details of a new VMachine :")
            
            
            data = get_vm_input()

            if data:
                count += 1
                VMs.append(data)  # Store the dictionary representation of the VM, VMs will store the Machine object (not its attributes). 
                logging.info(f"VM #{count} created with details: {data}")



        elif answer == "":
            logging.warning("No input received, user prompted again.")
            print("\nNothing was inserted, Please enter 'Yes' or 'No' !")

        else:
            logging.info("Configuration canceled by user.")
            print("\nConfiguration Canceled !")
            break

     

    logging.info(f"{count} VMs created.")
    logging.info("===== Session Ended =====")
    logging.info("-" * 100)
    

    print(f"\n{count} VM(s) created !\n")
    if count > 0:
        print("\nFinal List of Created VM(s):")
        for i in range(len(VMs)):                     # printing each VM only with its index.
            print(f"VM No: {i+1} : {VMs[i]}\n")
    else:
        None




if __name__ == "__main__":
    main()