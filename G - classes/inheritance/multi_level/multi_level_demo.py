class GrandParent:
    def show(self):
        print("Hai, I am Grandparent")

class Parent(GrandParent):
    def test(self):
        print("Hai, I am parent")

class Child(Parent):
    def dispaly(self):
        print("Hai, I am child")


c = Child()
c.show()
c.test()
c.dispaly()

