import logging
import threading
import time
import psutil
import numpy as np

delay=.0000001    # seconds
checkInterval=2
measurementInterval=1
targetUsage=input("What is the target percentage of CPU usage?")

runCheckCPU=True
runUseCPU=True

def checkCPU():
    global delay
    logging.info("checkCPU: starting")
    #make one measurement and throw it away
    cpuUsage=psutil.cpu_percent(interval=measurementInterval)
    while runCheckCPU:
        cpuUsage=psutil.cpu_percent(interval=measurementInterval)
        pct = int(targetUsage) / cpuUsage 
        delay = delay * pct
        logging.info("checkCPU: usage="+str(cpuUsage)+"  new delay="+str(delay))
        time.sleep(checkInterval-measurementInterval);
    logging.info("Thread %s: finishing", name)

def useCPU():
    logging.info("useCPU: starting")
    while runUseCPU:
        time.sleep(delay)
        x=np.random.rand(100,100)
        y=np.random.rand(100,100)
        z=np.dot(x,y)
        w=np.sort(z)
		# should put something here that uses some cpu
    logging.info("useCPU: ending")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : starting")
    checkThread = threading.Thread(target=checkCPU, args=())
    useThread = threading.Thread(target=useCPU, args=())
    checkThread.start()
    useThread.start()
    logging.info("Main    : all done")

