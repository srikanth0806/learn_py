"""13. Write a program that maps
a list of words into a list of integers representing
the lengths of that correponding words."""


def lenth_strings(li):
    list1 = []
    for i in li:
        x = len(i)
        list1.append(x)
    return list(zip(li,list1))

s=lenth_strings(["srikanth","gopi","murali","kondalu"])
print(s)
