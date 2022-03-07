
def test():
    print("i am test")
class Robot:
    A = 10
    def __init__(self, a):
        self.a = a

x = Robot(25)
y = Robot("y")

# print(Robot.A)
# print(x.A)
Robot.A = 100
x.A = 25
print(x.__dict__)
print(Robot.A)
print(y.A)
print(y.__dict__)