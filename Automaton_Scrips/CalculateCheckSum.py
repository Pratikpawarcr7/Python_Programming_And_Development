import sys
import os
import hashlib # CheckSum Calculate Krnyache Functions

def CalculateCheck_Sum(FileName):

    fobj = open(FileName,"rb") # Binary I/O (Chesum pahijay mhanun) (rb konti pn file) and (r only text (rwgular file))

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer)>0):
        hobj.update(Buffer) # Data Update Kr (1000 new 1000(Buffered) Thoda tHoda De)
        Buffer = fobj.read(1000)
# Read Krnar 1000,update 2000
    fobj.close() # He kellay mule MD 5 la samjat jal ahe purn

    return hobj.hexdigest() # Hich ti Check Sum Ahe
    
def main():
    Ret = CalculateCheck_Sum("Demo.txt")

    print("Checksum of File is : ",Ret)
    
if __name__ == "__main__":
    main()

    