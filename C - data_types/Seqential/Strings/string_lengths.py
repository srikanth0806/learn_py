"""
   Find words which are greater than given length k
"""


def string_lenth(s, k):
    li = s.split()
    li1 = []
    for i in li:
        if len(i) > k:
            li1.append(i)

    return li1


print(string_lenth("Find words which are greater than given", 4))

