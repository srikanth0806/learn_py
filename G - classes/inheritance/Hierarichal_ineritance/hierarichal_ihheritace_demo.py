""" write a python programme to implement the hierarchal inheritance"""


class Parent:
    def test(self):
        print(" I am husband")


class Mom(Parent):
    def test1(self):
        print(" I am wife ")


class Son:
    def show(self):
        print(" I am son ")


class Daughter(Mom, Son):
    def display(self):
        print("I am a Daughter")


d = Daughter()
d.test()
d.test1()
d.show()
d.display()


