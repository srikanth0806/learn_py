"""
    Remove all duplicates from a given string in Python
"""


# def dup(s):
#     li = list(s)
#     x = li
#     for i in li:
#         for j in range(1, len(li)):
#             if i == x[j]:
#                  x.remove(x[j])
#     return str(x)
#
#
# print(dup("charaters"))


def dup(s):
    li = []
    for i in s:
        if i not in li:
            li.append(i)
    x = str(li)
    return x


print(dup("charaters"))
