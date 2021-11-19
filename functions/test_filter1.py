def is_even(a):
    return a % 2 == 0


li = [21, 22, 23, 24, 26, 27, 28, 29, 30]
evens = list(filter(is_even, li))
print(evens)


evens1 = list(filter(lambda a: a % 2 == 0, li))
res = evens1
print(res)