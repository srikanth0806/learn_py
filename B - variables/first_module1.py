a = 10
b = 20


def sum():
    return a+b
s = sum()
print(s)


def mul():
    a = 4
    global b
    b = 5
    return a * b
x = mul()


print(x)

print(a)
print(b)


