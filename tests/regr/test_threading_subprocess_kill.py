import threading
import time
import os
import psutil

def kill_p(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

def task(pid):
    kill_p(pid)
    print("end th")


    
if __name__ == '__main__':
    pid =os.getpid()
    print(pid)
    
    thread1 = threading.Thread(target=task,args=(pid,))
    thread1.start()

    time.sleep(10)

    print("End")
    