"""
   Python Program for Sum of squares of first n natural numbers
"""


def sum_square(n):
    x = 0
    for i in range(n + 1):
        x = x + i * i
        return x


print(sum_square(5))



# """ Python Program for Sum of squares of first n natural numbers"""
#
#
# def sum_cube(n):
#     x = 0
#     for i in range(n + 1):
#         x = x + i * i * i
#         return x
#
#
# print(sum_cube(5))

