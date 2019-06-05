import threading
from threading import Lock
import time
total = 0
Lock = Lock()
def add():
    global total
    # simulate the IO bound
    time.sleep(10)
    # make it thread safe
    Lock.acquire()
    for i in range(1000000):
        # simulate the CPU bound 
        total += 1
    Lock.release()

def desc():
    global total
    time.sleep(10)
    Lock.acquire()
    for i in range(1000000):
        total -= 1
    Lock.release()

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(total)