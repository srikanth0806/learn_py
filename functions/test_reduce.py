from functools import reduce

def sum(a, b):
    return a + b

x = [1,2,3,4,5,6]

res = reduce(sum, x)

print(res)