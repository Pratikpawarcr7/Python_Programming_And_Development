import os
import time
import psutil

def main():

    start_Time = time.perf_counter()

    netobj = psutil.net_io_counters()

    print("Network Usage Report")

    print("Sent : %.2f MB\n"%(netobj.bytes_sent / (1024 * 1024)))

    print("Receive : %.2f MB\n"%(netobj.bytes_recv / (1024 * 1024)))

    end_Time = time.perf_counter()

    print(f"Time Require : {end_Time-start_Time:.4f}Seconds")

if __name__ == "__main__":
    main()