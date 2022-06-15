"""
    Python Program to Check If a List is Empty
"""


def empty_list(li):
    if li == list():
        return True
    else:
        return False


print(empty_list([]))

print(empty_list([1,"srikanth", 4.5]))
