import psutil
import time
import threading
def checkCPU():
	cpuUsage=psutil.cpu_percent(interval=1)
	print(cpuUsage)
	return cpuUsage
def useCPU(interval=.000001):
	while True:
		time.sleep(interval)
		
checkCPU()
checkThread=threading.Thread(target=checkCPU)
checkThread.start()
useCPU()
useThread=threading.Thread(target=useCPU)
useThread.start()
time.sleep(10)
useThread.join()
checkThread.join()


