"""
Python | Count occurrences of an element in a list
"""


def element_occuences(li):
    for i in li:
        z = i
        if z == i :
            x = li.count(i)
            print(i, "-", x)


element_occuences([1, 2, 3, 4, 5, 5, 4, 3, 2, []])
