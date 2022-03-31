"""
 write a python programme to explain the classmethod
"""


#type - 1 or old process

class Student:

    college_name = "jkc"

    def display(self):
        print(self.college_name)


Student.display=classmethod(Student.display)
s = Student()
s.display()
# or #
Student.display()


#type - 2 or new process

class Student:

    college_name = "jkc"

    @classmethod
    def display(cls):
        print(Student.college_name)
         #  or  #
        print(cls.college_name)


s = Student()
s.display()
# or #
Student.display()




