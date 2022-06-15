""" This is an example programe for multiple inheritance"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name


class Human:
    def __init__(self, age=0):
        pass

class Employee(Human, Person):
    def __init__(self, name, age, emp_no, designation, sal):
        self.emp_no = emp_no
        self.designation = designation
        self.salary = sal
        Person.__init__(self, name, age)
        Human.__init__(self)
        #super().__init__(name, age)
        #super(Employee, self).__init__(name, age)

    def get_emp_designation(self):
        return self.designation


emp = Employee("naga", 31, 1234, "Software", 10000)

print(emp.get_name())
print(emp.get_emp_designation())
