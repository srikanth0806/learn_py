"""
   this is a demo programme on polymorphism on functions.


   in below info() and make_sound are two methods in two different
   objects but working is similar.
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("my name is ", self.name)
        print("my age is ", self.age)

    def make_sound(self):
        print("meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("my name is ", self.name)
        print("my age is ", self.age)

    def make_sound(self):
        print("bou")


c1 = Cat("chinnu", 2)
d1 = Dog("bannu",4)

for i in (c1, d1):
    i.info()
    i.make_sound()
