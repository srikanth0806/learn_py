"""
 write a python programme to perform the abstraction concept.
"""

from abc import ABC, abstractmethod


class AbsClass(ABC):
    @abstractmethod
    def display(self):
        None

    @abstractmethod
    def show(self):
        None
    def test(self):
        None

class Demo(AbsClass):
    def display(self):
        print(" this display method is abstract method ")

class Demo1(AbsClass):
    def show(self):
        print("this show method is abstractmetod")
    def display(self):
        print(" this display method is abstract method ")


D = Demo()
print(D.dislay())