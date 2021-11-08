class robot1:
    A =30
    def __init__(self, b):
        self.b = b


x = robot1(90)
print(x.b)
print(x.A)
print(robot1.A)
#print(robot1.b)
x.b =200
print(x.b)

y = robot1(80)
print(y.b)
print(x.__dict__)
print(y.__dict__)
print(y.__dir__())
#




from cls_student import Student

x = Student("naga", 34, "mpc")

x.get_vals()
x.set_name("chandra")
x.get_vals()
x.course = "bipc"
x.age = 25
x.get_vals()

from cls_robot import Robot, test

test()


