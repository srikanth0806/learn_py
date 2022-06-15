"""
   Find length of a string in python (4 ways)
"""


# def string_length(s):
#     n = len(s)
#     return n
#
#
# print(string_length("definition"))

def string_length(s):
    for m in s:
        n = s.index(m)
    return n + 1


print(string_length("definition"))

