import threading
import time
import time
import os

def fun1():
    r=input('Choose a number')

t = threading.Thread(target = fun1)
t.start()
time.sleep(602)
raise "you shall not pass"
os._exit