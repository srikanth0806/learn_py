"""
 write a python programme to perform escape when you reach one number
"""


def fun(l):
    x = 25
    for i in l:
        if i == x:
            continue
        print(i)


fun([1, 3, 4, 5, 6, 7, 8, 9, 25, 34, 56, 78, 90])
