import pandas as pd

def main():

    sobj = pd.Series([2916000,32000,35000],index = ["Pratik","Pranay","Ashish"])

    print(sobj)  

    print(sobj["Pratik"])  

if __name__ == "__main__":
    main()