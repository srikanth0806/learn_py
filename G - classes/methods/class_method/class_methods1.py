from datetime import date

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthDate(cls, name, year):
        return cls(name, date.today().year-year)

    @staticmethod
    def isAdult(age):
        return age>18

x=Person("srikanth",27)
y=Person.fromBirthDate("srikanth",1994)
print(x.age)
print(y.age)
print(Person.isAdult(27))

