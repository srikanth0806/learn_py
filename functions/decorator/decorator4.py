def add_num(func):
    def sum_num():
        print("sum of two numbers")
        y = func()
        return y
    return sum_num


@add_num
def hello():
    x = 2
    y = 8
    z = x + y
    return z


# print(hello())
# print("-----------")
# hello = add_num(hello)
# print(hello())
print(hello())