import psutil
import logging
import time
import threading
import sys
monitoring=True
def monitorSystem():
	cpuUsage=[]
	memUsage=[]
	diskUsage=[]
	diskIo=[]
	while monitoring:
		cpuUsage.append(psutil.cpu_percent(1))
		print("Current CPU %: "+str(psutil.cpu_percent(1)))
		memUsage.append(psutil.virtual_memory()[2])
		print("Current memory stats are: ")
		print(psutil.virtual_memory())
		print(psutil.disk_usage('/'))
		diskUsage.append(psutil.disk_usage('/')[3])
		time.sleep(5)
	totalCpu=0
	totalMem=0
	totalDisk=0
	for item in cpuUsage:
		totalCpu+=item
	for item in memUsage:
		totalMem+=item
	for item in diskUsage:
		totalDisk+=item
	avgMem=totalMem/(len(memUsage))
	avgCPU=totalCpu/(len(cpuUsage))
	avgDisk=totalDisk/(len(diskUsage))
	print("Average CPU Utilization was: "+str(avgCPU))
	print("Average memory utilization was: "+ str(avgMem))
	print("Average disk usage was: "+str(avgDisk))
if __name__=="__main__":
	try:
		monitoringInterval=sys.argv[1]
	except:
		monitoringInterval=input("How many minutes do you want to monitor CPU and Memory usage?")
	t1=threading.Thread(target=monitorSystem, args=())
	t1.start()
	time.sleep(int(monitoringInterval)*60)
	monitoring=False
	
