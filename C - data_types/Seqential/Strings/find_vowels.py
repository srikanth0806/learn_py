"""
    Python program to accept the strings which contains all vowels
"""


def vowels(s):
    s = s.lower()
    s1 = ""
    for i in s:
        if i in ["a", "e", "i", "o", "u"]:
            s1 = s1 + i
    if s == s1:
        print("the string is accepted")
    else:
        print("the string is not accepted")


print(vowels("ae"))
print(vowels("python"))

