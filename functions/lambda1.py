"""
  23.Python Program to Find Numbers
  Divisible by Another Number.
"""


def f(li):

    return list(filter(lambda x : x % 4 == 0, li))


x = f([2, 12, 16, 25, 24, 71, 46])
print(x)