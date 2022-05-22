import threading as thread
import time

def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(threadName,time.ctime(time.time()) )

try:
    a = thread.Thread( target = print_time, args = ("Thread-1", 2) )
    b = thread.Thread( target = print_time, args = ("Thread-2", 4) )

    a.start()
    b.start()
    a.join()
    b.join()
    
except:
   print("Error: unable to start thread")

