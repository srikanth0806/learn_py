class A:
    x = 10
    y = 20


class B(A):
    a = 25
    b = 30


class C(B):
    pass


obj = A()

print(obj.x)
print(obj.y)
# print(obj.a)


obj2 = B()
print(obj2.x)
print(obj2.y)
print(obj2.a)
print(obj2.b)
