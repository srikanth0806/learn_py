"""
   Python | Reversing a List
"""

# using the slicing concept

# def rev_list(li):
#     x = li[::-1]
#     return x
#
#
# print(rev_list([1, 2, 3, 4, 5, "srikanth"]))


# using only while loop:

# def rev_list(li):
#     n = len(li)
#     li1 = []
#     i = 1
#     while i <= n:
#         li1.insert(i, li[-i])
#         i = i + 1
#
#     return li1
#
#
# print(rev_list([1, 2, 3, 4, 5, 6]))




# by using the for and while loop

def rev_list(li):
    li1 = []
    n = len(li)
    j = 0
    for i in li:
        while j < n:
            j = j + 1
            break
        li1.insert(-j, i)
    return li1


print(rev_list([1, 2, 3, 4, 5]))





