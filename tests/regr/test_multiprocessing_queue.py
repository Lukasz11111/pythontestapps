from multiprocessing import Process, Queue

revdebug.setrecmode(revdebug.Live)
revdebug.flush()  # compensating for live recording deletion on server

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()