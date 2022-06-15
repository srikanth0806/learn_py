"""
    write a python programme to take the substrings from a big string
     which are formed by all vowels
"""


def take_sub(s):
    x = s.lower()
    l = x.split()
    l1 = []
    print(l)
    for word in l:
        print(word)
        s1 = ""
        for i in word:
            if i in ["a", "e", "i", "o", "u"]:
                s1 = s1 + i
        if word == s1:
            l1.append(word)
    return l1


print(take_sub("write a python programme to take the substrings ae"))