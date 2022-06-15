"""
 write a python programme to skip or remove the letters from a list.
"""


def num(s, n):
    l = list(s)
    l.pop(n)
    x = str(l)
    return x


print(num("654378", 4))
