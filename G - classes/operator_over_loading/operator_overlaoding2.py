class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a - other.a, self.b - other.b


s = A(20, 10)
y = A(30, 40)
print(s + y)
