#!/usr/bin/env python

import revdebug  # linter kibble

revdebug.setrecmode(revdebug.Crash)

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

class mylist(list):
    pass

i = mylist([1, 2, 3])
i[1] = -2

i = i

def b():
    raise "You shall not pass!"

prev = revdebug.recrepr(mylist, lambda a: b())
i = i

# x = lambda a : b()
# print(x(3))