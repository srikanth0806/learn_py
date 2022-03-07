"""
 write the programme or working of the zip function.
"""


x = [1, 2, 3, 4, 5]
y = ["srikanth", "gopi", "murali", "kondalu", "kumar"]
F = [6,7,8,9]

zipped = zip(x, y)  #here, zipped in  the form of tuple look  in for
# print(zipped)
# for i in zipped:
#     print(i)
# for i, j in zipped:
#     print(i, j)

G = zip(x + F)
for i in G:
    print(i)


# zip convertion in different data types

A = list(zip(x, y))
print(A)
for i in A:
    print(i)
for i, j in A:
     print(i, j)


B = tuple(zip(x, y))
print(B)
for i in A:
    print(i)
for i, j in B:
     print(i, j)


D = dict(zip(x, y))
print(D)
for i in D:
     print(i)


E = set(zip(x, y))
print(E)
for i in E:
     print(i)