def outer():

    x = 3

    def inner():
        y = 4
        result = x + y
       # print(result)
        return result
    return inner


s = outer()
s()
print(s())