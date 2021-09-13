#!/usr/bin/env python

import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    q = mp.Queue()
    p = mp.Process(target = foo, args = (q,))
    p.start()
    print(q.get())
    p.join()
