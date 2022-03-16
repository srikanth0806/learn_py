"""
   Python Program to Illustrate Different Set Operations.

       i.intersection
       ii.union
       iii.difference

"""

A = {1, 2, 3, 4, 5}
B = {8, 7, 3, 2, 1, 6}


def set_operations():
    print("union of A and B is :", A | B)
    print("intersection of A and B is :", A & B)
    print("difference between A and B is :", A - B)
    print("symmetric difference between A and B is :", A ^ B)


set_operations()