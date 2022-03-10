"""
    write a python programe to show the findall methods executions
"""

import re

s = "There is a possibility that the string contains " \
    "lowercase and upper case"
result = re.findall(r"\w{5}", s, re.IGNORECASE)
print(result)