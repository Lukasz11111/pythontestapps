
import time
import sys
import test_err_in_def as err
import os

class x:
    def v():
        i=100
a=time.sleep(1)

revdebug.record(time)

revdebug.record("err")

revdebug.record(err)

revdebug.record(ValueError)

revdebug.record(os.path)

print("NO rec")

revdebug.norecord(time)

revdebug.norecord("err")

revdebug.norecord(err)

revdebug.norecord(ValueError)

revdebug.norecord("/*")

print("set rec")

revdebug.setrecord(x,"True")

revdebug.setrecord(x,ValueError)

print("END")