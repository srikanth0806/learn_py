"""
 write a prgrame to create a  dictionary, by using
how many times the strings are occures in a data or a large string.
"""


def tree():
    s = "What is a good piece of content? Good content is original What"
    words = s.split()  # here, s is a large string.
    print(words)       #when we use the split method , the words to be a list.
    print(words.count("What"))
    x = dict()
    for i in words:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    return x


print(tree())