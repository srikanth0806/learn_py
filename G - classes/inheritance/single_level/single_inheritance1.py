class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Human:
    def __init__(self, experiance):
        self.experiance = experiance


class Employee(Person, Human):

    def __init__(self, name, age, experiance, company_name, designation):
        self.company_name = company_name
        self.designation = designation
        Person.__init__(self, name, age)

        Human.__init__(self, experiance)

    def get_company_name(self):
        return self.company_name

    def set_comapny_name(self, company_name):
        self.company_name = company_name


emp = Employee("srikanth", 27, 3, "wipro", "software")
print(emp.get_company_name())
emp.set_comapny_name("HCL")
print(emp.get_company_name())








