"""creating a Thread  by extending Thread class."""

from threading import *


class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("child thread")


mt = MyThread()   #  creating the child thread
mt.start()        # starting the child thread and this is applicable
                  # to run() method

for i in range(10):
    print("main thread")   # this code is under main thread