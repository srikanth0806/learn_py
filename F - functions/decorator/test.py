

def power(func):
    x = func()
    x = int(x)
    return x ** 2


@power
def take_input():
    a = input("enter a value: ")
    return a

x = power(take_input)
x()