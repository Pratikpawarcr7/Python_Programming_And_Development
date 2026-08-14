# 4
def main():

    try:
#-----------------------------------------------------------------------------------------------------------------------
# File write krayechi ahe Demo.txt write & create krnay sathi "w"
#-----------------------------------------------------------------------------------------------------------------------
        fobj = open("Demo.txt","a")
        print("File gets Opened")

        fobj.write(" Pune Maharashtra")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if __name__ == "__main__":
    main()