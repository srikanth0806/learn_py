"""
Python Program to Extract Extension From the File Name

"""


# Type - 1:  Using splitext() method from os module

import os
file_details = os.path.splitext('test2.txt')
print(file_details)
print(file_details[1])


# Type - 2: Using pathlib module

import pathlib
x = pathlib.Path('test2.txt').suffix
print(x)