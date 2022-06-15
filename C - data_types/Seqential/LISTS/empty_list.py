"""
 Python – Remove empty List from List
"""


def empty_list(li):
    for i in li:
        if i == []:
            li.remove(i)

    return li


print(empty_list([1, 2, 3, 4, 5, 6, [], 7, 8, 9]))
