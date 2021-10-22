import time
while True:
    print("clear")
    revdebug.clear()
    print("setrecmode Live")
    revdebug.setrecmode(revdebug.Live)
    print("flush")
    revdebug.flush()
    print("setrecmode Crash")
    revdebug.setrecmode(revdebug.Crash)
