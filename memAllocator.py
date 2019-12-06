import os
import subprocess
import psutil
import time
import threading

num_of_blocks= input("How many megabyte blocks of memory do you want to consume?")
time_of_test=input("How long do you wish to consume the memory for in minutes?")
test_time_seconds=int(time_of_test)*60
byteSwitching=True
def byteArraySwitcher():
	while byteSwitching:
		print(psutil.virtual_memory())
		test1=bytearray(int(num_of_blocks)*250000)
		test2=bytearray(int(num_of_blocks)*250000)
		test3=bytearray(int(num_of_blocks)*250000)
		test4=bytearray(int(num_of_blocks)*250000)
		for i in test1:
			t1=test1[i]
			t2=test2[i]
			t3=test3[i]
			t4=test4[i]
			test1[i]=t2
			test2[i]=t1
			test3[i]=t4
			test4[i]=t3
		for i in test2:
			t1=test1[i]
			t2=test2[i]
			t3=test3[i]
			t4=test4[i]
			test1[i]=t2
			test2[i]=t1
			test3[i]=t4
			test4[i]=t3
					
byteSwitchThread=threading.Thread(target=byteArraySwitcher, args=())
byteSwitchThread.start()
print(psutil.cpu_percent())
print(psutil.virtual_memory())
time.sleep(int(test_time_seconds))
print(psutil.virtual_memory())
byteSwitching=False
byteSwitchThread.join()
print("Exiting program.")
