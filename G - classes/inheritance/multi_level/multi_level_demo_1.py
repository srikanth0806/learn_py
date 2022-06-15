"""
write a python demo programme for multilevel inheritance
"""


class Grand_Parent:
    def __init__(self, g_name, g_age):
        self.g_name = g_name
        self.g_age = g_age


class Parent(Grand_Parent):
    def __init__(self, p_name, p_age, g_name, g_age):
        self.p_name = p_name
        self.p_age = p_age
        Grand_Parent.__init__(self, g_name, g_age)


class Child(Parent):
    def __init__(self, name, age, p_name, p_age, g_name, g_age):
        self.name = name
        self.age = age
        Parent.__init__(self, p_name, p_age, g_name, g_age)

    # i am taking one example method on variables
    def get_p_name(self):
        return self.p_name

    def set_p_name(self, p_name):
        self.p_name = p_name


c = Child("deepu", 1, "nag", 30, "kondalu", 52)
print(c.get_p_name())
c.set_p_name("nag hero")

print(c.get_p_name())


