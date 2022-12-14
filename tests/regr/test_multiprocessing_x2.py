#!/usr/bin/env python

import multiprocessing as mp
import time
import sys

def f(z):
    z.put('bye')

def foo(q):
    z = mp.Queue()
    p = mp.Process(target = f, args = (z,))
    p.start()

    q.put(str(z.get()))
    p.join()


if __name__ == '__main__':
    revdebug.setrecmode(revdebug.Live)
    revdebug.flush()  # compensating for live recording deletion on server

    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target = foo, args = (q,))

    p.start()
    print(q.get())
    p.join()

    time.sleep(0.3)
    


