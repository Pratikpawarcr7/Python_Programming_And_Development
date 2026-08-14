import sys
import os
import hashlib # CheckSum Calculate Krnyache Functions

def CalculateCheck_Sum(FileName):

    fobj = open(FileName,"rb") # Binary I/O

    hobj = hashlib.md5()

    Buffer = fobj.read(1024) # Jevda asl tevda de

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024) # suppose 1000 dela tr 24 remainin and ntr prat 1000 read krnar 48remaini (Hard Disk = Block, RAM = Page (Both 1kb))

    fobj.close()

    return hobj.hexdigest() # Hich ti Check Sum Ahe ( 1a88f20756104dd343405e22464dac42 (Hexadecimal Number Ahe)return 32 byte )

def main():
    Ret = CalculateCheck_Sum("DemoX.txt")

    print("Checksum of File is : ",Ret)

if __name__ == "__main__":
    main() 