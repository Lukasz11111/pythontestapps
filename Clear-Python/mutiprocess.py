from multiprocessing import Process, Lock
import time
# revdebug.setrecmode(revdebug.Live)
# revdebug.flush()  # compensating for live recording deletion on server

def f(l, i):
    l.acquire()
    time.sleep(5)
    try:
        print('hello world', i)
        raise 'YOu Shall not pass'
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):

        Process(target=f, args=(lock, num)).start()