"""
   write a python programme to print multiplication.
"""

def mul(n):
    i = 1
    y = 2
    while i <= n:
        x = y * i
        i = i + 1
        yield x


m = mul(10)
for i in m:
    print(i)