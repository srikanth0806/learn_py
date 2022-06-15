# Write a Python program to multiply all the items in a list


def list_mul(items):
    mul = 1
    for i in items:
        mul *= i
    return mul


print(list_mul([1, 2, 7]))
print(list_mul([1, 3, "srikanth"]))
print(list_mul([1, 3, [9, 7], "srikanth"]))



# by using the numpy :

# # Python3 program to multiply all values in the
# # list using numpy.prod()
#
# import numpy
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
#
# # using numpy.prod() to get the multiplications
# result1 = numpy.prod(list1)
# result2 = numpy.prod(list2)
# print(result1)
# print(result2)


# by using the math:

# # Python3 program to multiply all values in the
# # list using math.prod
#
# import math
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
#
#
# result1 = math.prod(list1)
# result2 = math.prod(list2)
# print(result1)
# print(result2)


# # by using the lambda function:
#
# # Python3 program to multiply all values in the
# # list using lambda function and reduce()
#
# from functools import reduce
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
#
#
# result1 = reduce((lambda x, y: x * y), list1)
# result2 = reduce((lambda x, y: x * y), list2)
# print(result1)
# print(result2)
