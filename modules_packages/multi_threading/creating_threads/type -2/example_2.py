import time
from threading import *


class Hello(Thread):

    def start(self):
        for i in range(50):
            print("Hello")
            time.sleep(1)


class Hai(Thread):

    def start(self):
        for i in range(50):
            print("Hai")
            time.sleep(1)


h = Hello()
h1 = Hai()

h.start()
time.sleep(0.2)
h1.start()

h.join()
h1.join()

print("Bye")
