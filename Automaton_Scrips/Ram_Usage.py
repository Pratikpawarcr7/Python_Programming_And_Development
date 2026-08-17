import os
import time
import psutil

def main():

    start_Time = time.perf_counter()
    memory = psutil.virtual_memory()
    print("Ram Usage : %s %%" % memory.percent)
    end_Time = time.perf_counter()


    print(f"Time Require : {end_Time-start_Time:.4f}Seconds")

if __name__ == "__main__":
    main()