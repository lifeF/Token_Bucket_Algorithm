import time, threading
def foo():
    print(time.ctime())
    threading.Timer(10, foo).start()

foo()
