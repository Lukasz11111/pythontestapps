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



def b():
    b()


prev = revdebug.recrepr(mylist, lambda a: b(i))
print("a1")
i = i
print("a2")
i = i
raise "Err"
