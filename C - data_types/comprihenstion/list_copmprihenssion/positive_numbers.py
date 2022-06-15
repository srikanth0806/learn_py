"""
   Python program to print positive numbers in a list
"""


# def positive(li):
#     for i in li:
#         if i > 0:
#             print(i)
#
#
# positive([1, -2, 3, -4, 5, -6, 7, -8, 9, -10])


# type - 2 : list comprihension

def positive(li):

    li1 = [num for num in li if num > 0]
    return li1


print(positive([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))
