"""
   Sort the values of first list using second list in Python
"""


def sort_list(li,li1):
    ziped_lists = zip(li1, li)
    print(ziped_lists)
    z = {x for k, x in sorted(ziped_lists)}
    return z



x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))

# x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
# y = [0, 1, 1, 0, 1, 2, 2, 0, 1]
#
# print(sort_list(x, y))

