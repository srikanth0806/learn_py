class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def get_name(self,name):
        return self.name

    def set_name(self,name):
        self.name = name


class Human:
    def __init__(self,experiance):
        self.experiance=experiance


class Employee(Person, Human):

    def __init__(self,name,age,company_name,designation):
        self.company_name = company_name
        self.designation=designation
        Person.__init__(self,name, age)

        Human.__init__(self, experiance=3)

    def get_company_name(self):
        return self.company_name

    def get_designation(self):
        return self.designation

    def set_sal(self):
        self.sal= 1500




emp=Employee("srikanth",27,"wipro","software")
print(emp.get_company_name())
print(emp.get_designation())








