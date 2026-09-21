import pandas as pd

def main():
#--------------------------------------------------------------
# Every Series is the List But Every List is Not The Series
#--------------------------------------------------------------
    sobj = pd.Series([11,21,51,101],index = ["C","C++","Java","Python"])

    print(sobj)  

    print(sobj["Python"])  

if __name__ == "__main__":
    main()