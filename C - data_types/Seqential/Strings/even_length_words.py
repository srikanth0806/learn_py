"""
    Python program to print even length words in a string
"""


def even_length_words(s):
    x = s.split()
    l = []
    for i in x:
        n = len(i)
        if n % 2 == 0:
            l.append(i)

    return l


print(even_length_words("List Programs: Python program"
                        "to interchange first and last elements in a list"))
