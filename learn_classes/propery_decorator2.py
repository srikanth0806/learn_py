"      PROPETY CONCEPT IN CLASSES    ,  MODEL-2  ,  EXAMPLE-1    "
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def peru(self):
        return self.name

    @peru.setter
    def peru(self, new_name):
        self.name = new_name

    @peru.deleter
    def peru(self):
        del self.name

std = Student("naga", 31)
print(std.peru)
std.peru = "srikanth"
print(std.peru)
