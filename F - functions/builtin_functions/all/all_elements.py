"""write a python programme to perform the all() fnction.

diefinition:
    The all() function returns True if all items in an iterable are true,
     otherwise it returns False.

    If the iterable object is empty, the all() function also returns True.

Syntax:
      all(iterable)
      iterable	(may be) ----> list, tuple, dictionary

"""


a = [1, 2, 3, 4, 5, 6]

b = [1, 2, 3, 4, -46, 5]

c = [1, 2, 3, 4, -46, 5, []]

d = [True, True, True, True]

e = [True, True, False, True]

print(all(a))
print(all(b))
print(all(c))
print(all(d))
print(all(e))