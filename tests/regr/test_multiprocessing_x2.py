
#!/usr/bin/env python
from multiprocessing import Pool
import multiprocessing as mp
import time

def f(x):
    print("a")
    return x*x

def foo(q):
    with Pool(5) as z:
        print(z.map(f, [1, 2, 3]))
    q.put('hello')
    time.sleep(0.2)

if __name__ == '__main__':
    revdebug.setrecmode(revdebug.Live)
    revdebug.flush()  # compensating for live recording deletion on server

    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target = foo, args = (q,))

    p.start()
    print(q.get())
    p.join()

    time.sleep(0.1)