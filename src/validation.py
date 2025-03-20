
import ipaddress

def Name_Validation(Name):

        allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"

        while True:
            try:
                for i in Name:
                        if i not in allowed_characters:
                            raise ValueError("Invalid character found.")
            
                return Name  # If no issues, return the valid name.

            except ValueError as e:
                print(e)  # Prints the custom error message.
                Name = input("Please enter a valid VM name in the format : [ VM name - number]: ").strip().lower()



def OS_Validation(OS):
        
        OperatingSystem = ("Windows","Linux","Mac")

        while True:
            try:
                if  OS not in OperatingSystem:
                    raise ValueError ("Invalid Operating System entered.")
        
                return OS
        
            except ValueError as e:
                print(e)
                OS = input("Please enter a valid Operating-System [ Windows, Linux, Mac ] : ")


def CPU_Validation(CPU):
     
        while True:
            try:
                  CPU = int(CPU)
                  if 1 <= CPU <= 64 :
                       return CPU
                  else:
                       raise ValueError ("Invalid number amount of cores of the CPU entered.")
                  
            except ValueError as e:
                 print(e)
                 CPU = input("Please enter a valid number amount of cores of the CPU ( 1 - 64 ) : ")


def GPU_Validation(GPU):
     
        GPU_Vendors = ("Nvidia","AMD","Intel")

        while True:
            try:
                if  GPU not in GPU_Vendors:
                    raise ValueError ("Invalid GPU-Vendor entered.")
        
                return GPU
        
            except ValueError as e:
                print(e)
                GPU = input("Please enter a valid GPU-Vendor [ Nvidia, AMD, Intel ] : ")



def RAM_Validation(RAM):
     
     while True:
            try:
                  RAM = int(RAM)
                  if 1 <= RAM <= 256 :
                       return RAM
                  else:
                       raise ValueError ("Invalid RAM-Memory entered.")
                  
            except ValueError as e:
                 print(e)
                 RAM = input("Please enter a valid RAM-Memory ( 0 - 256 )GB : ")


def Disk_Validation(Disk):
        
        while True:
            try:
                  Disk = int(Disk)
                  if 1 <= Disk <= 500 :
                       return Disk
                  else:
                       raise ValueError ("Invalid Disk-Storage-Memory entered.")
                  
            except ValueError as e:
                 print(e)
                 Disk = input("Please enter a valid Disk-Storage-Memory ( 0 - 500 )GB : ")


def IP_Validation(IP):
     while True:
        try:
                ip = ipaddress.ip_address(IP)
                return ip
        except ValueError as e:
             print(e)
             IP=input("Please enter a valid IP-Address [ Format : 0-255.0-255.0-255.0-255 ] : ")


