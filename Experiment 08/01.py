<<<<<<< HEAD
import threading
x = 0     # A shared value
COUNT = 10
def incr():
    global x
    for i in range(COUNT):
        x += 1
        print(x)
def decr():
    global x
    for i in range(COUNT):
        x -= 1
        print(x)
t1 = threading.Thread(target=incr)
t2 = threading.Thread(target=decr)
t1.start()
t2.start()
t1.join()
t2.join()
print(x)
=======
import threading
x = 0     # A shared value
COUNT = 10
def incr():
    global x
    for i in range(COUNT):
        x += 1
        print(x)
def decr():
    global x
    for i in range(COUNT):
        x -= 1
        print(x)
t1 = threading.Thread(target=incr)
t2 = threading.Thread(target=decr)
t1.start()
t2.start()
t1.join()
t2.join()
print(x)
>>>>>>> c7462266bf5bbe709727b07d9e164f25601f4cf7
