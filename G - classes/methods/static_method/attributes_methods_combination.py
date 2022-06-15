"write a python programme on inheritance."


class A:
    # below x,y --> class variables or attributes
    x = 10
    y = 20

    # below a,b --> instance variables or attributes, methods --> instance methods
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_values(self):
        print(self.a, self.b)

    def addition_two(self):
        sum = self.a + self.b
        print(sum)

    # below method --> class method
    @classmethod
    def subtraction_two(cls):
        sub = cls.y - cls.x
        print(sub)

    @staticmethod
    def multiplication_two(l, m):
        mul = l * m
        print(mul)


class B(A):
    z = 80


b = B(30, 40)
print(b.x)
print(b.y)
b.get_values()
b.addition_two()
b.subtraction_two()
b.multiplication_two(6, 7)

