class Robot:
    A = 30

    def __init__(self, b):
        self.b = b


x = Robot(90)
print(x.b)
print(x.A)
print(Robot.A)
#print(Robot.b)
x.b = 200
print(x.b)

y = Robot(80)
print(y.b)
print(x.__dict__)
print(y.__dict__)
print(y.__dir__())
#




from learn_classes.classes_basic_programs.cls_student import Student

x = Student("naga", 34, "mpc")

x.get_vals()
x.set_name("chandra")
x.get_vals()
x.course = "bipc"
x.age = 25
x.get_vals()

from learn_classes.classes_basic_programs.cls_robot import test

test()


