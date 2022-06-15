"""
   Python Program Read a File Line by Line Into a List
"""


def file_read_list(fname, mode):
    with open(fname, mode) as f:
        li = f.readlines()
        return li


print(file_read_list("test2.txt", "r"))
