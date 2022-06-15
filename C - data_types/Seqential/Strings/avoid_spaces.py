"""
    Python – Avoid Spaces in string length
"""


def avoid_spaces(s):
    x = ""
    for i in s:
        if i == " ":
            continue
        else:
            x = x + i
    return x


print(avoid_spaces("the final string is "))
