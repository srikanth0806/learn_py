"""Python Program to Parse a String to a Float or Int"""


def parse_string(s):
    x = int(s)
    y = float(s)
    return x, y


print(parse_string("23"))
