"""
adding aplhabets to anoyher string.
"""


def apphabets(s):
    l = []
    temp = ""
    i = 0
    while i < len(s):
        n = i
        n1 = n + 1
        for x in range(n, n1):
            temp = temp + s[i]
            print(temp)
        l.append(temp)
        i = i + 1
    print(l)


apphabets("abcdefghijklmnopqrstuvwxyz")
