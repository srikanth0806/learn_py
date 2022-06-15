"""
 write a python programme to skip or remove the letters from a string.
"""

def num(s, n):
    x = len(s)
    i = 0
    temp = ""
    while i < x:
        if i == n:
            # continue -----> what is the problem ?
            s.replace(s[i], "")

        else:
            temp = temp + s[i]

        i = i + 1

    return temp


print(num("654378", 4))