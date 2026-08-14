# 9 ( Read Krnay Sathi )
# seek(kuthe,kuthun)
# Kuthon : 0/1/2

# 0 Starting
# 1 Current
# 2 End

def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")

        fobj.seek(10,0) # (Marvellous (ignor Honar)) Infosystem Pune Maharashtra
    
        Data = fobj.read()

        print(Data)

    except FileNotFoundError as fobj:
        print("File is not present in current directory")
        
if __name__ == "__main__":
    main()