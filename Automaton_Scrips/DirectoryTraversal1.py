#-------------------------------------------------------------------------------------
#
# jela  aapn folder bolto typa aapn prograamming language madhi directrory mhanto
# 2types of path : 1) Absulute Path :- root pasun sangitla jatoh
#                  2) Relative Path :-   
#
#--------------------------------------------------------------------------------------

import os

def main():
    for FolderName , SubFolder, FileName in os.walk("Marvellous"):
        print(FolderName)

if __name__ == "__main__":
    main()