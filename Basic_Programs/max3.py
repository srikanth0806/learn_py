"""

    Define a function max() that takes three numbers as arguments and
      returns the largest of them.

      we can solve  by 4 types.

"""


# type -1 : by using max() bultin function

# a = 10
# b = 14
# c = 12
# print(max(a, b, c))


#Logic -2:

# def maximum(a, b, c):
#     if (a >= b) and (a >= c):
#         largest = a
#
#     elif (b >= a) and (b >= c):
#         largest = b
#     else:
#         largest = c
#
#     return largest
#
#
# print(maximum(10, 14, 13))

    
#Logic - 3:

import pdb


def max_num(a, b, c):
    if a > b:
        if a > c:
            return "a is big"
        else:
            return "c is big"
    else:
        return "b is big "


pdb.set_trace()
x = max_num(5, 15, 10)
print(x)




#logic - 4 :


# import pdb
#
#
# def max_of_two(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# def max_of_three(x, y, z):
#     return max_of_two(x, max_of_two(y, z))
#
#
# pdb.set_trace()
# print(max_of_three(3, 6, -5))



# note :
# def maximum(a, b, c):
#     list = [a, b, c]
#     return max(list)

