#!/usr/bin/env python

import revdebug  # linter kibble

revdebug.setrecmode(revdebug.Crash)

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

class mylist(list):
    pass

i = mylist([1, 2, 3])
i[1] = -2

i = i
import time
def b():
    time.sleep(0.1)
    return "go go"
    

prev = revdebug.recrepr(mylist, lambda self: f'{b()} poewr rangers'  )
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
i = i
raise "You shall not pass!"