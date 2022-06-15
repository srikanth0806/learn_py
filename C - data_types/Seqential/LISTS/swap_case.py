"""
    Python program to swap two elements in a list
"""


def swap_two_elements(li):
    temp = li[3]
    li[3] = li[5]
    li[5] = temp

    return li


print(swap_two_elements([5, 6, 7, "gopi", 5, "srikanth", 3, 2]))

