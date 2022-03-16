"""
    Python Program to Remove Punctuations From a String.

    punctuations:

"""


def pun(s):

    if s.isalnum == True:
        return s
    else:
        li = s.split()
        x = ""
        for i in li:
            if i == i.isalnum():
                x = x + i
                return x

print(pun("srikanth#!"))
