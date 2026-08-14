#-----------------------------------------------------
# Baherun AAnl (pip install ni)
#-----------------------------------------------------
import schedule 
#-----------------------------------------------------
# thread la sleep sathi time import kela
#-----------------------------------------------------

import time  
import datetime

def Display():
    print("Jay Ganesh...",datetime.datetime.now())

def main():
    print("Automation Script Started") 

#-----------------------------------------------------
# dar eks minitani Display method Call kr
#-----------------------------------------------------
    schedule.every(1).minute.do(Display) 


# While b'coz thread jiwant thevnay sathi    
    while True:
#-----------------------------------------------------------------------------------------------------------------------
# Display Navacha call Run_Pending Mule Janar ahe
#-----------------------------------------------------------------------------------------------------------------------
        
        schedule.run_pending()  

#------------------------------------------------------------------------------------------------------------------------
   #
# seconds (#time.sleep(1) he task haych secondala Run Hoyeil Aas nahi) (pudh nonar maag nahi) 2 second eetra jale hotay
# 60 vela jaun yenar
#
#-------------------------------------------------------------------------------------------------------------------------    
        time.sleep(1)  
    
    print("End of automation")
  
if __name__ == "__main__":
    main()
  

  # jeva aapn ctr + c press krtoh teva te aaplication aapn sota off krto know as keyboard Interrupt meand Miroprocessessor aapli ti process kill krtoh
