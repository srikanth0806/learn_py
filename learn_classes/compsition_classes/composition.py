"        '  COMPOSITION OF CLASSES '             "


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name


class Human:
    def __init__(self, name, age):
        self.per = Person(name, age)

    def get_name(self):
        return self.per.get_name()

    def set_name(self,name):
        self.per.set_name = name


h = Human("rama", 1000)
print(h.get_name())
print(h.set_name("krishna"))
print(h.get_name())
