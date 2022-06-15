"""creating a thread without using any class."""

from threading import *


def display():
    for i in range(10):
        print("child thread")


t = Thread(target=display)  # creating the child thread
t.start()      # ------------> starting the child thread

for i in range(10):       # this is in main thread
    print("main thread")
