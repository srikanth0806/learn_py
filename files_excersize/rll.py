# Write a Python program to read a file line by line and store it into a list.
def read_lines(fname):
    with open(fname) as f:
        a=f.readlines()
        print(a)
read_lines("test2.txt")