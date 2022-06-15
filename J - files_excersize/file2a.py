#Write a Python program to read first n lines of a file.
def r_n(fname,number):
    from itertools import islice
    for line in islice(open(fname),number):
           print(line)
r_n("test2.txt",5)