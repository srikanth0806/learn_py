#Write a Python program to read first n lines of a file.
def r_n(fname,number):
    from itertools import islice
    with open(fname) as f:
       for line in islice(f,number):
           print(line)
r_n("test2.txt",5)