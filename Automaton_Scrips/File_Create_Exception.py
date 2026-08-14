# 5
def main():

    try:
#-----------------------------------------------------------------------------------------------------------------------
# File write krayechi ahe Demo.txt write & create krnay sathi "w"
#-----------------------------------------------------------------------------------------------------------------------
        open("Demo.txt","w")
        print("File gets Opened")

    except FileNotFoundError as fobj: # File Nsl tr Exception Yet Mhanun AApn Hyb Lihla  
        print("File is not Present in Current Directory")

if __name__ == "__main__":
    main()