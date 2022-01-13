import threading
import time

def task(event):
  print("Started thread but waiting for event...")

  event.wait()
  raise "err"
    
if __name__ == '__main__':
    # initializing the event object
    e = threading.Event()
    
    # starting the thread
    for i in range(0,10):
        threading.Thread(name=f'Event-Blocking-Thread{i}', target=task, args=(e)).start()

    e.set()
    print("Event is set.")
  