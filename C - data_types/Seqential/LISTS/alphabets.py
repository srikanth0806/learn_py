"""
 write a python programme to separate the list into  sublists as elements
"""

def alphabets(s):
    li = list(s)
    print(li)

    temp = []
    n = len(s)
    i = 0
    j = 1

    while i < n:
        x = i + j
        temp.append(li[i:x])
        i = x
        j = j + 1

    return temp


print(alphabets("abcdefghijklmnopqrstuvwxyz"))