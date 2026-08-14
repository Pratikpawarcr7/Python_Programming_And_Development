# Garbeg Collector 

import schedule # Baherun AAnl (pip nii)
import time  # thread la sleep sathi time import kela
import datetime

def Display():
    print("Jay Ganesh...",datetime.datetime.now())

def main():
    print("Automation Script Started")  

    schedule.every(1).minute.do(Display) # dar eks minitani Display method Call kr (Display la aapn Bracket Nahi takli bcoz Te pending call krnar jr Bracket takli tr Aapn call krtoy sota)

    while True:
        schedule.run_pending()  # Display Navacha call Run_Pending Mule Janar ahe
        time.sleep(1) # seconds (#time.sleep(1) he task haych secondala Run Hoyeil Aas nahi) (pudh nonar maag nahi) 2 second eetra jale hotay
    # 60 vela jaun yenar
    print("End of automation")
  
if __name__ == "__main__":
    main()
  
