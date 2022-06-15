"""
   Python | Maximum frequency character in String
"""


def max_frequency(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    k = d.values()
    n = max(k)
    for key, value in d.items():
        if value == n:
            return key


print(max_frequency("maximum frequency"))
