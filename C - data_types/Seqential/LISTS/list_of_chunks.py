"""
   Break a list into chunks of size N in Python
"""


def chunks(li, n):
    x = []
    for i in range(0, len(li), 3):
        x.append(i)
    return x


print(chunks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))


