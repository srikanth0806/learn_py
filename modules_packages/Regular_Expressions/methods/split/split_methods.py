"""
    write a python programe to perfrom the split method in regex
"""


import re

s = "There is a possibility that the string contains " \
    "lowercase the upper case"
result = re.split(r"the", s, re.IGNORECASE)
print(result)
