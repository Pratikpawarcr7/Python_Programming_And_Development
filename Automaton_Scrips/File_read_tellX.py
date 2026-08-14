# 8 ( Read Krnay Sathi )
def main():

    try:

        fobj = open("Demo.txt","r")
        print("File gets Opened")

        print("File offset is : ",fobj.tell())  # 0
        Data = fobj.read(10) # Purn Rerad Kral

        print(Data)

        print("File offset is : ",fobj.tell()) # 10

        Data = fobj.read(10) # Marvellous chy pudhchy 10 Rerad Kral
        
        print(Data)
        
        print("File offset is : ",fobj.tell())

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if __name__ == "__main__":
    main()