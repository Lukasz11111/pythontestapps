import time

@revdebug.norecord
def a():
    p=1
    name="a"
    revdebug.snapshot(name)
    time.sleep(0.02)

a()