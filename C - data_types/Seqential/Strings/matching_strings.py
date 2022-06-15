"""
   Python | Count the Number of matching characters in a pair of string
"""


def matching(s, s1):
    se = set()
    for i in s:
        for j in s1:
            if i is j:
                se.add(i)

    li = list(se)
    n = len(li)
    return n


print(matching("matching", " characters"))
