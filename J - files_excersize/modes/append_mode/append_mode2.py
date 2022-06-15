"""
    Python Program to Append to a File
"""


def append_mode(fname):
    with open(fname, "a") as f:
        f.write("  \n i am append some text")

append_mode("test2.txt")