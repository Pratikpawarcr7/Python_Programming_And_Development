import pandas as pd

def main():

    Data = [11,21,51,101]

    print(Data)
#-------------------------------------
# Create the Series (pd.series)
#--------------------------------------
    sobj = pd.Series(Data)

    print(sobj)    

if __name__ == "__main__":
    main()