from pydantic import BaseModel,Field,IPvAnyAddress,ValidationError

class VMachine(BaseModel):

    Name : str = Field(...,pattern = r'^[a-zA-Z0-9-_]+$',description ="Name format must be : [ VM name - number]")
    OS : str = Field(...,pattern=r'^(Windows|Linux|Mac)$', description = "Operating-System must be : ( Windows, Linux, Mac )")
    CPU : int = Field(...,ge=1,le=64,description="CPU must be between : 1 - 64")
    GPU : str = Field(...,pattern=r'^(Nvidia|AMD|Intel)$',description = " GPU must be : ( Nvidia, AMD, Intel )")
    RAM : int = Field(...,ge=1,le=256,description="RAM Memory must be (0 - 256)GB")
    Disk : int = Field(...,ge=1,le=500,description="Disk Storage must be (0 - 500)GB)")
    IP : IPvAnyAddress 

    # In Pydantic v2, the regex parameter has been replaced by the 'pattern' parameter in the Field() function.

def get_vm_input():
        try:
            # collect user input
            Name = input("\nEnter a valid VM name in the format : [ VM name - number]: ").strip()
            OS = input("Choose an Operating-System : ( Windows, Linux, Mac ) : ").strip()
            CPU = int(input("Enter the number of cores of the CPU ( 1 - 64 ) : "))
            GPU = input("Choose GPU vendor ( Nvidia, AMD, Intel ) :  ").strip()
            RAM = int(input("Enter RAM Memory in GB (0 - 256) :  "))
            Disk = int(input("Enter Disk Storage in GB (0 - 500) : "))
            IP = input("Enter an IP Adress ( 0-255.0-255.0-255.0-255 ) : ")  # i removed 'int' because pydantuc handles with string automatically.

            # validate inouts using pydantic
            vm = VMachine(Name=Name,OS=OS, CPU=CPU,GPU=GPU,RAM=RAM, Disk=Disk, IP=IP)
            print("\nVM Created Successfully:\n", vm)
            return vm

        except ValidationError as e:
            #print("\nValidation Error:\n", e)
            print("\nValidation Error(s):")
            for error in e.errors():
                    print(f"- {error['loc']}: {error['msg']}")


        except ValueError:
            print("\nInvalid input! Please enter numbers where required.")


        except TypeError:
            print("\nUnexpected input type! Please follow the required format.")