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
