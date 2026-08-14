# 5 ( Read Krnay Sathi )
def main():

    try:

        fobj = open("Demo.txt","r")
        print("File gets Opened")

        Data = fobj.read(10) # 0 to 10 read kra  (byte vach toh sagle charector 1 byte che astat)

        print(Data)

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if __name__ == "__main__":
    main()