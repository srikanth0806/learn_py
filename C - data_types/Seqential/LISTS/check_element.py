"""
    Python | Ways to check if element exists in list
"""


def check_element(li, x):
    if x in li:
        return True
    else:
        return False


print(check_element([1, 2, 3, 4, 5,"srikanth"], "srikanth"))
print(check_element([1, 2, 3, 4, 5,"srikanth"], "nag"))


# -------------or --------------------------#


def element_check(li, x):
    for i in li:
        if x == i:
            return True
        else:
            return False


print(check_element([1, 2, 3, 4, 5,"srikanth"], "srikanth"))
print(check_element([1, 2, 3, 4, 5,"srikanth"], "nag"))



# **************** or ****************** #


def ele_find(li, s):
    n = li.count(s)
    if n > 0:
        return "the element is existed"
    else:
        return "the element is not existed"


print(ele_find([1, 2, 3, 4, 5, 6, "srikanth"], "srikanth"))





