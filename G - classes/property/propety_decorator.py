"      PROPETY CONCEPT IN CLASSES    ,  MODEL-1  ,  EXAMPLE-1    "
class Student:
    def __init__(self, name, age, course="mca"):
        self.name = name
        self.age = age
        self.course = course

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def del_name(self):
        del self.name

    naam = property(get_name, set_name, del_name, "this is a propery for name")

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def del_age(self):
        del self.age

    vayasu = property(get_age, set_age, del_age)


std = Student("naga", 31)
print(std.naam)
std.naam = "srikanth"
print(std.naam)

# del std.naam

print(std.vayasu)
std.vayasu = 40
print(std.vayasu)