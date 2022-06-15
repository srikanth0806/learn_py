"""
write a python programme to print the how many times the substrings
occures in a given string.
"""


#s = "how are you"

def fun(s):
    d = dict()
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    return d


print(fun("how are you"))
