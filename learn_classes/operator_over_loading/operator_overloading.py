class A:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return self.x + other.x ,self.y + other.y
    def __sub__(self, other):
         return self.x - other.x,self.y - other.y


obj1 = A(10, 20, 30)
obj2 = A(1,2,3)
obj3 = A(5,6,7)

print(obj1 + obj2 )

