"""
    find the negative numbers in a list.
"""


# def negative_num(li):
#     for i in li:
#         if i < 0:
#             print(i)
#
#
# negative_num([1, -3, 4, -5, 6, -7])


# or #

# type - 2 : list comprihension


def negative_num(li):
    x = [num for num in li if num < 0]
    return x


print(negative_num([1, -3, 4, -5, 6, -7]))
