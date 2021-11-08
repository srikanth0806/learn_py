from collections import namedtuple

student = namedtuple("student", "name rool_no study")

x = student("naga", "12345", "ssc")

print(x[0])
