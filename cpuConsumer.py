import math
import logging
import threading
import time
import psutil
import numpy as np
import datetime
import sys
from random import randint
delay=.0000001    # seconds
checkInterval=2
measurementInterval=1

runCheckCPU=True
runUseCPU=True

def checkCPU():
    global delay
    logging.info("checkCPU: starting")
    #make one measurement and throw it away
    cpuUsage=psutil.cpu_percent(interval=measurementInterval)
    while runCheckCPU:
        cpuUsage=psutil.cpu_percent(interval=measurementInterval)
        pct =cpuUsage/ int(targetUsage)  
        delay = delay * pct
        logging.info("checkCPU: usage="+str(cpuUsage)+"  new delay="+str(delay))
        time.sleep(checkInterval)
    logging.info("Thread %s: finishing")

def useCPU():
    logging.info("useCPU: starting")
    while runUseCPU:
        time.sleep(delay)
        y=randint(0,1000000)
        print(math.sqrt(y))
    logging.info("useCPU: ending")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    try: 
        cpuConsumptionInterval=sys.argv[1]
    except:
        cpuConsumptionInterval=input("How many minutes do you want to consume CPU for?")
    try: 
        targetUsage=sys.argv[2]
    except:
        targetUsage=input("What is the target percentage of CPU usage?")       
    logging.info("Main    : starting")
    checkThread = threading.Thread(target=checkCPU, args=())
    x = threading.Thread(target=useCPU, args=())
    x.start()
    y = threading.Thread(target=useCPU, args=())
    y.start()
    checkThread.start()
    time.sleep(int(cpuConsumptionInterval)*60)
    runCheckCPU=False
    runUseCPU=False	
    logging.info("Main    : all done")

