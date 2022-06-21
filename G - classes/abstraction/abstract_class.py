#abstract class.
from abc import ABC, abstractmethod

class Person(ABC):
    
    def get_name(self):
        return "naga"

    @abstractmethod
    def set_name(self, new_name):
        pass


class Human(Person):
    def hello(self):
        return "hello"

    def set_name(self, new_name):
        print("my name is ", new_name)

h = Human()
h.set_name("sikanth")
print(h.get_name())
print(h.hello())
