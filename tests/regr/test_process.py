import subprocess
import time
import psutil
process = subprocess.Popen('python tests/regr/test_async_sleep.py', shell=True)
print(process.pid)

time.sleep(4)

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

kill(process.pid)
