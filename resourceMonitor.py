import psutil
import logging
import time
import threading
monitoring=True
def monitorSystem():
	cpuUsage=[]
	memUsage=[]
	while monitoring:
		cpuUsage.append(psutil.cpu_percent())
		memUsage.append(psutil.virtual_memory()[2])
		time.sleep(5)
	totalCpu=0
	totalMem=0
	for item in cpuUsage:
		totalCpu+=item
	for item in memUsage:
		totalMem+=item
	avgMem=totalMem/(len(memUsage))
	avgCPU=totalCpu/(len(cpuUsage))
	print(avgCPU)
	print(avgMem)

if __name__=="__main__":
	monitoringInterval=input("How many minutes do you want to monitor CPU and Memory usage?")
	t1=threading.Thread(target=monitorSystem, args=())
	t1.start()
	time.sleep(int(monitoringInterval)*60)
	monitoring=False
	
