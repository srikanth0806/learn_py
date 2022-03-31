class Student:
    def __init__(self, name, age, course="mca"):
        self.__name = name
        self._age = age
        self.course = course

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self._age

class Humans(Student):
    def __init__(self, name, age, course, gender="male"):
        super().__init__(name, age, course)
        self.gender = gender


h = Humans("naga", 31, "bsc")

#print(h.__dict__)
print(h.course)
print(h._age)
print(h.get_name())
h.set_name("sri")
print(h.get_name())
