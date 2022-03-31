"""
   write a python programme to perform the static method
"""


class Addition:

    @staticmethod
    def sum(x,y):     # here , no use self or cls parameters
        print("the sum of x and y :", x + y)


a = Addition()
a.sum(5,4)
# or #
Addition.sum(5,4)