#!/user/bin/env python3

import threading
import time

def func1():
	for ii in range(100):
		print(1)
def func2():
	for ii in range(100):
		print(2)



th1 = threading.Thread(target=func1,name='func1',args=())
th2 = threading.Thread(target=func2,name='func2',args=())


th1.start()
th2.start()


