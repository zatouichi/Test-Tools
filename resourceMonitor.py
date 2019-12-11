import psutil
import logging
import time
import threading
import sys
monitoring=True
def monitorSystem():
	cpuUsage=[]
	memUsage=[]
	while monitoring:
		cpuUsage.append(psutil.cpu_percent(1))
		print("Current CPU %: "+str(psutil.cpu_percent(1)))
		memUsage.append(psutil.virtual_memory()[2])
		print("Current memory stats are: ")
		print(psutil.virtual_memory())
		time.sleep(5)
	totalCpu=0
	totalMem=0
	for item in cpuUsage:
		totalCpu+=item
	for item in memUsage:
		totalMem+=item
	avgMem=totalMem/(len(memUsage))
	avgCPU=totalCpu/(len(cpuUsage))
	print("Average CPU Utilization was: "+str(avgCPU))
	print("Average memory utilization was: "+ str(avgMem))

if __name__=="__main__":
	if sys.argv[1] != None:
		monitoringInterval=sys.argv[1]
	else:
		monitoringInterval=input("How many minutes do you want to monitor CPU and Memory usage?")
	t1=threading.Thread(target=monitorSystem, args=())
	t1.start()
	time.sleep(int(monitoringInterval)*60)
	monitoring=False
	
