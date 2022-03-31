sum_two = lambda x, y: x + y

result = sum_two(5, 6)

print(result)
print(type(sum_two))

def big_of_two(x, y):
    return x if x > y else y

test_of_two = big_of_two

print(test_of_two(8, 10))

print(id(big_of_two), id(test_of_two))

my_func = lambda a, b: a - b
print(my_func(23, 22))
