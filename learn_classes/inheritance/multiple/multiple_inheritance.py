
class A:
    x = 10
    def test(self):
        print("I amm from A")

class B:
    x = 20
    def test(self):
        print("I amm from B")

class C(B, A):
    x = 30
    def test(self):
        print("I amm from C")

c = C()
print(c.x)
c.test()
print(C.__mro__)
