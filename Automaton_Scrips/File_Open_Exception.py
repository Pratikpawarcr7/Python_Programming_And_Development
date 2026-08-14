# 2
# File asl tr tii except madhi janar ahe
def main():

    try:
        open("Demo.txt","r")
        print("File gets Opened")

    except FileNotFoundError as fobj:
        print("File is not Present in Current Directory")

if __name__ == "__main__":
    main()