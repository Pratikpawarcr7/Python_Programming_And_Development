# 3

def main():

    try:
#-----------------------------------------------------------------------------------------------------------------------
# File write krayechi ahe Demo.txt write & create krnay sathi "w"
#-----------------------------------------------------------------------------------------------------------------------
        fobj = open("Demo.txt","w")
        print("File gets Opened")

        fobj.write("Jay Ganesh...")

        fobj.close()

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if __name__ == "__main__":
    main()

#-----------------------------------------------------------------------------------------------------------------------
# Duble Double Write kela tr data Ovrride Hoto te risky ahe mahnun FIle)Create writeX
#-----------------------------------------------------------------------------------------------------------------------

