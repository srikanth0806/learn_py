"""
Python Program to Remove Duplicate Element From a List.
"""


def remove_duplicates(li):
    x = set(li)
    y = list(x)
    return y


print(remove_duplicates(["srikanth", 1, 3, 4, 5, "gopi", 5.5, "srikanth"]))
