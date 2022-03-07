def func_addtion():
    num = 1
    while num < 10:
        num += 1
    return num
addtion_value = func_addtion()
print(addtion_value)
print(type(addtion_value))
def gene_addition():
    num = 1
    while num < 10:
        num += 1
        yield num
add_value = gene_addition()
print(type(add_value))
# try:
#      while True:
#          print(next(add_value))
# except StopIteration:
#      pass

for i in add_value:
    print(i)

print(" programme completed")