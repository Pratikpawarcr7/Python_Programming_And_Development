import sys
import os
import hashlib # CheckSum Calculate Krnyache Functions

def Calculate_Check_Sum(FileName):

    fobj = open(FileName,"rb") # Binary I/O

    hobj = hashlib.md5()

    Buffer = fobj.read(1024) # Jevda asl tevda de

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024) # suppose 1000 dela tr 24 remainin and ntr prat 1000 read krnar 48remaini (Hard Disk = Block, RAM = Page (Both 1kb))

    fobj.close()

    return hobj.hexdigest() # Hich ti Check Sum Ahe ( 1a88f20756104dd343405e22464dac42 (Hexadecimal Number Ahe)return 32 byte )

def Find_Duplicated(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is Invalid")
        return

    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is Not a Directory")
        return

    Duplicate = {}

    Unique = 0
    Same = 0


    for FolderName,SubFolder,FileName in os.walk(DirectoryName):
        for fName in FileName:
            fName = os.path.join(FolderName,fName) # Jodun Path Anun DEtoh

            CheckSum = Calculate_Check_Sum(fName)

            print(f"{fName} : {CheckSum}")

            if CheckSum in Duplicate:
                Same = Same + 1
                Duplicate[CheckSum].append(fName)
            else:
                Unique = Unique + 1
                Duplicate[CheckSum] = [fName]
                
    print("Unique Files found :",Unique)
    print("Duplicate files Found :",Same)

def main():
   Find_Duplicated("Test")
            
if __name__ == "__main__":
    main() 

    