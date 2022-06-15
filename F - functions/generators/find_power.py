"""
   write a python programme to find the poweres of given range of number.
"""

# generator :

def power(n):
    for i in range(1, n + 1):
        yield i ** 2


p = power(5)

for i in p:
    print(i)