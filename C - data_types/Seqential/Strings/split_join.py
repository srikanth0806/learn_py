"""
    Python program to split and join a string
"""


def split_join(s):
    li = s.split()
    print(li)
    # s1 = ""
    # for i in li:
    #     s1 = s1 + i
    # return s1"
    s1 = "-".join(li)
    return s1

print(split_join("Python program to split and join a string"))