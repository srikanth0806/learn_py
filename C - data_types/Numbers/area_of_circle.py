#  7.write a Python Program  to find area of a circle
import math


def area_circle(r):
    pi = 3.142
    a = pi * pow(r, 2)
    return a


y = area_circle(5)
print(y)
