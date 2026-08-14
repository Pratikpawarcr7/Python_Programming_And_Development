import sys  # Command Line Argument Sathi 
import os
import time
import schedule

Border = "-"*40
def DirectoryScanner(DirectoryPath = "Marvellous"):
    timestamp = time.ctime() # new

    LogFileName = "Marvellous%s.log"%(timestamp)  #  MarvellousTue Jul 28 10:57:07 2026.log
    LogFileName = LogFileName.replace(" ","_")  # ( replace kela space " " to "_")MarvellousTue_Jul_28_11:00:18_2026.log
    LogFileName = LogFileName.replace(":","_")

    print("Log File gets created with name : ",LogFileName)

    fobj = open(LogFileName,"w")
    fobj.write(" Marvellous Automation Script \n")
    
    for FolderName,SubFolderName,FileName in os.walk(DirectoryPath):
         for fname in FileName:  
              fobj.write(fname+"\n")

    
    fobj.write(Border+"\n")
    fobj.write("Log file gets created at : " + timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()

def main():

     print(Border)
     print(" Marvellous Automation Script ")
     print(Border)

     if(len(sys.argv) == 2):
        if (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script Used to Travel the Directory")
            print("For Better Usage please check --u flag ")

        elif (sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please Excute the Script as")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path") # Surwat raoot pasun jali pahijay
        
        else:
                
                schedule.every(1).minutes.do(DirectoryScanner,sys.argv[1])  # First is Name Of Function And Second Should Be Parameter

                while True:
                     schedule.run_pending()
                     time.sleep(1)

              #  DirectoryScanner(sys.argv[1])

     else:
         print("Invalid Number of Arguments")
         print("Please use --h or --u for more information")

     print(Border)
     print(" Thank you for using Marvellous Automation Script ")
     print(Border)
            
if __name__ == "__main__":
    main()


    # pip pip instal Pacakage (recursive acronium)

    # This Project Run on Server (thire is Lots Of File in =)