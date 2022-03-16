class A:
    x = 10
    def test(self):
        print("I amm from A")

class B(A):
    x = 20
    def test(self):
        print("I amm from B")

class C(B):
    x = 30
    def test(self):
        print("I amm from C")


    # def test(self, a):
    #     print("I amm from c second time")
    #
    # def test(self, a, b):
    #     print("I amm from c third time")

# a = A()
# print(A.x)
# a.test()

b = B()
print(B.x)
b.test()

# c = C()

#c.test()
#c.test(5)
# c.test(3,10)
