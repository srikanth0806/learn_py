"""creating a Thread  by exending Thread class."""
from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("child thread")
t=MyThread()
t.start()

for i in range(10):
    print("main thread")