# """
#    writet a python programme to explain
#    the instance method and class method
# """
#
# class Expla():
#     school_name = "Abc school"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         return self.name, self.age
#
#     def change_details(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def change_school(cls, school_name):
#         cls.school_name = school_name
#
#
# e = Expla("srikanth", "vivekananda")
# print(e.show())
# print(Expla.school_name)
#



# def add(fun):
#     def display():
#         print("before addition")
#         x = fun()
#         print("after addition", x)
#
#     return display
#
# @add
#
# def show():
#     x = 4
#     y = 5
#     return  x + y
#
# print(show())



