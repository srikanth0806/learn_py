"""
 this is an example programme for encapsulation.

 definition:
            Encapsulation in Python describes
            the concept of bundling data and methods
            within a single unit.

            for example, when you create a class,
            it means you are implementing encapsulation.
            A class is an example of encapsulation as it binds
            all the data members (instance variables) and methods
            into a single unit.
"""


class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)


# creating object of a class
emp = Employee('Nag', 120000, 'intel')

# calling public method of the class
emp.show()
emp.work()