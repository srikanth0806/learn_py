"""
    Python | Check if a Substring is Present in a Given String
"""


def in_opertator(s, sub_string):
    if sub_string in s:
        return True
    else:
        return False


print(in_opertator("srikanth", "ka"))
print(in_opertator("srikanth", "w"))

