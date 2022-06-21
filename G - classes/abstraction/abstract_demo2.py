"""
 write a python programme to perform the abstraction concept.
"""

from abc import ABC, abstractmethod


class AbsClass(ABC):
    def print(self, x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("We are inside Absclass task")


class Test_Class(AbsClass):
    def task(self):
        print("We are inside test_class task")


class Example_Class(AbsClass):
    def task(self):
        print("We are inside example_class task")


# object of test_class created
test_obj = Test_Class()
test_obj.task()
test_obj.print(100)

# object of example_class created
example_obj = Example_Class()
example_obj.task()
example_obj.print(200)

print("test_obj is instance of Absclass? ", isinstance(test_obj, AbsClass))
print("example_obj is instance of Absclass? ",
      isinstance(example_obj, AbsClass))
