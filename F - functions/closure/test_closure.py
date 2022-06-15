
def my_func(a, b):
    print(a, b)
    def power():
        nonlocal a
        nonlocal b
        a = 20
        b = 30
        print("a is %d, b is %d" % (a, b))

    return power
x= my_func(5, 6)
print(x)