from functools import reduce
li = [45, 67, 89, 56, 34, 300]
sub_values = reduce(lambda a, b: a-b, li)
res = sub_values
print(res)