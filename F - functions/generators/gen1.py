def my_func(*args):
     x = list()
     for i in args:
         x.append(i ** 2)
     return x
 func_val = my_func(1, 2, 3, 4, 5, 6, 7, 8)

def my_gen(*args):
    for i in args:
        yield i ** 2


gene_obj = my_gen(1, 2, 3, 4, 5, 6, 7, 8)
print(type(gene_obj))
print("----------------")
print(dir(gene_obj))
print("----------------")
try:
    while True:
        print(next(gene_obj))
except StopIteration:
    pass

print("completed")
