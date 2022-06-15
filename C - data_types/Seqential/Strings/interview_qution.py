"""
write a programme sum of the digits
"""


def fun(n):
    s = str(n)
    l = len(s)
    sum = 0
    for i in range(l):
        sum = sum + int(s[i])
    x = int(sum)
    return x


print(fun(456))
