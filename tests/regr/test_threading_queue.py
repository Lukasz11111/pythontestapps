import threading, queue
import time
q = queue.Queue()


revdebug.setrecmode(revdebug.Live)
revdebug.flush()

def a():
    def worker():
        while True:
            item = q.get()
            print(f'Working on {item}')
            print(f'Finished {item}')
            q.task_done()


    # turn-on the worker thread
    threading.Thread(target=worker, daemon=True).start()

    # send thirty task requests to the worker
    for item in range(5):
        q.put(item)
        # time.sleep(1)
    print('All task requests sent\n', end='')

    # block until all tasks are done
    q.join()
    print('All work completed')


def b():
    def worker():
        while True:
            revdebug.clear()
            item = q.get()
            print(f'Working on {item}')
            print(f'Finished {item}')
            q.task_done()
            revdebug.snapshot(str(item))


    # turn-on the worker thread
    threading.Thread(target=worker, daemon=True).start()

    # send thirty task requests to the worker
    for item in range(5):
        q.put(item)
        # time.sleep(1)
    print('All task requests sent\n', end='')

    # block until all tasks are done
    q.join()
    print('All work completed')



def c():
    q = queue.Queue(maxsize=1)
    def worker():
        while True:
            time.sleep(1)
            item = q.get()
            print(f'Working on {item}')
            print(f'Finished {item}')
            q.task_done()
            revdebug.snapshot("Worker"+ str(item))

    # turn-on the worker thread
    threading.Thread(target=worker, daemon=True).start()

    # send thirty task requests to the worker
    for item in range(5):
        q.put(str(item)+"Q")
    raise "You shall not pass"
    print('All task requests sent\n', end='')

    # block until all tasks are done
    q.join()
    print('All work completed')

def d():
    q1 = queue.Queue()
    q2 = queue.Queue()
    q3 = queue.Queue()
    def worker1():
        while True:
            item = q1.get()
            print(f'Working on {item}')
            print(f'Finished {item}')
            q1.task_done()
            revdebug.snapshot("Worker"+ str(item))
    def worker2():
        while True:
            item = q2.get()
            print(f'Working on {item}')
            print(f'Finished {item}')
            q2.task_done()
            revdebug.snapshot("Worker"+ str(item))
    def worker3():
        while True:
            item = q3.get()
            print(f'Working on {item}')
            print(f'Finished {item}')
            q3.task_done()
            revdebug.snapshot("Worker"+ str(item))

    # turn-on the worker thread
    threading.Thread(target=worker1, daemon=True).start()
    threading.Thread(target=worker2, daemon=True).start()
    threading.Thread(target=worker3, daemon=True).start()


    # send thirty task requests to the worker
    for item in range(3):
        time.sleep(1)
        q1.put(str(item)+"Q1")
        time.sleep(1)
        q2.put(str(item)+"Q2")
        time.sleep(1)
        q3.put(str(item)+"Q3")
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
# d()