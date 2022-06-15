"""
 write a python programme to combine  list elements to seperate list
 elements
"""


def elements(li):
    temp = []
    j = 0
    x = 1
    while x <= len(li):
        li1 = []
        while j < x:
            li1.append(li[j])
            j = j + 1
        temp.append(li1)
        x = x + 3

    return temp


print(elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
