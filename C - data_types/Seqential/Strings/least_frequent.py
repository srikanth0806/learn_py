"""
    Python – Least Frequent Character in String
"""


def least(s):
    li = []
    for i in s:
        if s.count(i) == 1:
            li.append(i)
    return li


print(least("srikanthrikanth"))




