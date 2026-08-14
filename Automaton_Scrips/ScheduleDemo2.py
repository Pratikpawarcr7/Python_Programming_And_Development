import schedule # Baherun AAnl (pip nii)
import time  # thread la sleep sathi time import kela
import datetime

def Display():
    print("Jay Ganesh...",datetime.datetime.now())

def main():
    print("Automation Script Started")  

    schedule.every(1).minute.do(Display) # dar eks minitani Display method Call kr

    # Issue

if __name__ == "__main__":
    main()
  
