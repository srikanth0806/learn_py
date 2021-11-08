"""15. Write a function filter_long_words() that takes
a list of words and an integer n and
returns the list of words that are longer than n"""

def filter_long_words(li,n):
    empty_list = []
    for i in li:
        if len(i)>n:
            empty_list.append(i)
    return empty_list
s=filter_long_words(["srikanth","gopi","murali","kondalu"],5)
print(s)