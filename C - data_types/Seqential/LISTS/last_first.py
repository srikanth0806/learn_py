"""
   Python program to interchange first and last elements in a list
"""


def interch(li):
    print(li)
    x = li[0]
    li[0] = li[-1]
    li[-1] = x
    print(li)


interch([1, 2, 3, 4, 5])


# ------------- or -------------------#


def swap_ele(li):
    print(li)
    x = li.pop(0)
    y = li.pop(-1)
    li.insert(0, y)
    #li.insert(-1, x)  #  you good logic in this
    li.append(x)
    
    return li


print(swap_ele([1, 2, 3, 4, 5]))
