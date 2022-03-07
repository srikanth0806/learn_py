def power(func):
    def inner():
        x = func()
        x = int(x)
        return x ** 2
    return inner

@power
def take_input():
    a = input("enter a value: ")
    return a
print(take_input())
       # OR #
# my_dec = power(take_input)
# x = my_dec()
# print(x)

# take_input = power(take_input)
#print(take_input())
