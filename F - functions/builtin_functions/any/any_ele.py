"""write a python programme to perform the all() fnction.

diefinition:
    The any() function returns True if any items in an iterable are true,
     otherwise it returns False.

    If the iterable object is empty, the any() function also returns False.

Syntax:
      any(iterable)
      iterable	(may be) ----> list, tuple, dictionary

"""


a = [1, 2, 3, 4, 5, 6]

b = [1, 2, 3, 4, -46, 5]

c = ["", {},  []]

d = [True, True, True, True]

e = [False, False]

print(any(a))
print(any(b))
print(any(c))
print(any(d))
print(any(e))