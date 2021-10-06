import threading
import time
def a():
    sem = threading.Semaphore()

    def fun1():
        for x in range(1,10):
            sem.acquire()
            print(str(x)+"fun1")
            sem.release()
            time.sleep(3)
            
            
            

    def fun2():
        for x in range(1,10):
            sem.acquire()
            print(str(x)+"fun2")
            sem.release()
            
            time.sleep(1)

    revdebug.setrecmode(revdebug.Live)
    revdebug.flush()

    t = threading.Thread(target = fun1)
    t.start()
    t2 = threading.Thread(target = fun2)
    t2.start()

def b():
    sem = threading.Semaphore()

    def fun1():
        for x in range(1,10):
            sem.acquire()
            print(str(x)+"fun1")
            sem.release()
            time.sleep(3)
            raise "You shall not pass!"
            
            
            

    def fun2():
        for x in range(1,10):
            sem.acquire()
            print(str(x)+"fun2")
            sem.release()
            
            time.sleep(1)

    revdebug.setrecmode(revdebug.Live)
    revdebug.flush()

    t = threading.Thread(target = fun1)
    t.start()
    t2 = threading.Thread(target = fun2)
    t2.start()

a()
b()