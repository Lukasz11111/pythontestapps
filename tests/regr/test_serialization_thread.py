#!/usr/bin/env python

import revdebug  
import threading


revdebug.setrecmode(revdebug.Live)

revdebug.flush() 

class mylist(list):
    pass

i = mylist([1, 2, 3])
i[1] = -2

i = i

def thread_function():
    a=0

def b():
    print("c")
    threading.Thread(target = thread_function).start()

prev = revdebug.recrepr(mylist, lambda a: b())
print("a1")
i = i
print("a2")
i = i
raise "Err"
