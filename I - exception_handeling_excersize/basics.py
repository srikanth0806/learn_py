
try:
    x = int(input("enter a number1:"))
except ValueError:
    print("x values must be integer")
    x = 1

try:
    y = input("enter a number2:")
except ValueError:
    print("y values must be integer")
    y = 1
except ArithmeticError:
    print("arithmetic error handled")

try:
    val = x / y
except ZeroDivisionError:
    print("y value should not be zero")

print(val)

print("hi")
print("hello")
