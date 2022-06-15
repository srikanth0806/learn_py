"""
    Python | Ways to find length of list
"""


def find_lenth(li):
    n = len(li)
    return n


print(find_lenth([1, 2, 3, 4, 5, 6, "srikanth"]))



# -------------------------- or ----------------------------- #


def len_find(li):
    count = 0
    for i in li:
        count = count + 1
    return count


print(len_find([1, 2, 3, 4, 5, 6, "srikanth"]))












