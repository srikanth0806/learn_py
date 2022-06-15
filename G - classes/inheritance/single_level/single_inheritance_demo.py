class Parent:
    def show(self):
        print(" hai, I am a parent ")


class Child(Parent):
    def display(self):
        print("hai, I am a child")


c = Child()
c.show()
c.display()