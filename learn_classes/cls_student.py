class Student:
    def __init__(self, name, age, course="mca"):
        self.__name = name
        self.age = age
        self.course = course

    def get_vals(self):
        print(self.__name, self.age, self.course)

    def say_hello(self):
        print("good morning %s" % self.__name)

    def set_course(self, new_course):
        self.course = new_course

    def set_name(self, new_name):
        self.__name = new_name

    @staticmethod
    def test_even(x):
        if x%2 == 0:
            return True
        else:
            return False

# std1 = Student("nageswar", 31)
# std2 = Student("Srikanth", 26, "bca")

# print(std1.name)
# std1.name = "channdra"
# print(std1.name)
#
# std1.sex = "male"
#
# print(std1.__dict__)
# print(std2.__dict__)

# std1.get_vals()
# std1.set_course("Bipc")
# std1.get_vals()
#
# std1.course = "mpc"