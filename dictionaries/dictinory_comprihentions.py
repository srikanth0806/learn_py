#simple example
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
new_dict = {k: v for (k, v) in zip(keys, values)}
print(new_dict)


# with expression
s = {x: x*2 for x in [5, 4, 3, 2, 1]}
print(s)


# try  with condition

