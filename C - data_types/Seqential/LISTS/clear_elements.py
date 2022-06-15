"""
   Different ways to clear a list in Python
"""


def list_clear(li):
    print(li)
    li.clear()
    print(li)


list_clear([1, 2, 3, 4, 5])


# what happens in this below function?

def list_clear(li):

    print(li)
    for i in li:
        li.pop()
    return li


# here, in below line you can observe only two elements are removed
# means only 3 and 4 are removed remaining are not removed
# you know what happens in this?
print(list_clear([1, 2, 3, 4]))


# what happens in this below function?

def list_clear(li):
    x = li
    print(x)
    for i in x:
        li.remove(i)
    return x


print(list_clear([1, 2, 3, 4, 5, 6, 7]))

