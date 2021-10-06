import threading, queue
import time

def d():
    q1 = queue.Queue()
    q2 = queue.Queue()
    q3 = queue.PriorityQueue()
    def worker():
        while True:
            time.sleep(1)
            item = q1.get()
            item = q2.get()
            item = q3.get()
            print(f'Working on {item}')
            print(f'Finished {item}')
            q1.task_done()
            q2.task_done()
            q3.task_done()
            revdebug.snapshot("Worker"+ str(item))

    # turn-on the worker thread
    threading.Thread(target=worker, daemon=True).start()

    # send thirty task requests to the worker
    for item in range(3):
        time.sleep(0.5)
        q1.put(str(item)+"Q1")
        time.sleep(0.5)
        q2.put(str(item)+"Q2")
        time.sleep(0.5)
        q3.put(str(item)+"Q3P")
    # raise "You shall not pass"
    print('All task requests sent\n', end='')

    # block until all tasks are done
    q1.join()
    q2.join()
    q3.join()
    print('All work completed')

# a()
# b()
# c()
d()