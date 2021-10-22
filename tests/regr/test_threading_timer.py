import threading
def hello():
    raise "You shall not pass"

t = threading.Timer(10, hello)
t.start()