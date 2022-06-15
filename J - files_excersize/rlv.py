# Write a Python program to read a file line by line store it into a variable
def read_lines(fname):
    with open(fname,"r") as f:
        a=f.readlines()
        print(a)
read_lines("test2.txt")