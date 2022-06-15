"""" This is an example programme for multiple inheritance"""


class GrandParent:
    def show(self):
        print("Hai, I am Grandparent")


class Parent:
    def test(self):
        print("Hai, I am parent")


class Child(GrandParent, Parent):
    def dispaly(self):
        print("Hai, I am child")


c = Child()
c.show()
c.test()
c.dispaly()



