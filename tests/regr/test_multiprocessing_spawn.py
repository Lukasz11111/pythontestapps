#!/usr/bin/env python

import multiprocessing as mp
import time

def foo(q):
    q.put('hello')
    time.sleep(0.2)

if __name__ == '__main__':
    revdebug.flush()  # compensating for live recording deletion on server

    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target = foo, args = (q,))

    p.start()
    print(q.get())
    p.join()

    time.sleep(0.1)
