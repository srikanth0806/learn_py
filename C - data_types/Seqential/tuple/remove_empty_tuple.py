"""
Python | Remove empty tuples from a list
"""


def remove_empty_tuple(li):
    for i in li:
        if i == ():
            li.remove(i)

    return li


print(remove_empty_tuple([("ram", "lakshman"), (), (1, 2), (4.5)]))
