"""
  write a python programe to implementing the search method
"""

import re

s = "There is a possibility that the string contains " \
        "lowercase and upper case"
# below,re.IGNORECASE is a Flag used for ignoring the casesencitive
result = re.search(r"\w{5}", s, re.IGNORECASE)
print(result)
# given below  all in search methods
print(result.group())
print(result.groups())
print(result.groupdict())
print(result.start())
print(result.end())
#print(result.expand())
print(result.span())
print(result.__dir__())

#given below are functons in search method
print(result.string)
print(result.re)
print(result.pos)
print(result.endpos)
print(result.lastindex)
print(result.lastgroup)
print(result.regs)





result1 = re.findall(r"\w{5}", s, re.IGNORECASE)
print(result1)