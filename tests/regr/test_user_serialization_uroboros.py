#!/usr/bin/env python

import revdebug  

revdebug.setrecmode(revdebug.Crash)

revdebug.flush() 

class mylist(list):
    pass

i = mylist([1, 2, 3])
i[1] = -2

i = i

def b():
    revdebug.flush()
    revdebug.exception()
    revdebug.setrecmode(revdebug.Crash)
    revdebug.block()
    revdebug.snapshot("test")
    revdebug.snapshotall("test")
    revdebug.clear()
    revdebug.clearall()
    revdebug.record()
    revdebug.norecord()
    revdebug.setrecord()
    revdebug.recrepr()
    revdebug.snapshot('a')

prev = revdebug.recrepr(mylist, lambda a: b())
print("a1")
i = i
print("a2")
i = i
raise "Err"


