"""
   write a python programme to find the number and then terminate
"""


def fun(l):
    x = 25
    for i in l:
        print(i)
        if i == x:
            break


fun([1, 2, 3, 4, 5, 6, 25, 34, 56, 7, 78])
