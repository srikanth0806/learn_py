
def my_func(a, b):
    #print(a, b)
    def power():
        nonlocal a
        nonlocal b
        a = a**2
        b = b**3
        print("a is %d, b is %d" %(a, b))

    return power

closure = my_func(5, 6)

print(type(closure))
closure()