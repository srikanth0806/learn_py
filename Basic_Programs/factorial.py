"""
Python Program for factorial of a number.
factorial = n!, n * n-1 * n-2......*1
 there is a 4-types of code available in python
"""

# TYPE - 1 :  and this is my way and using recursion


def fact_num(n):
    if n < 0:
        return " the number is not exist"

    if n == 0 or n == 1:
        return 1

    else:
        return n * fact_num(n - 1)


print(fact_num(5))


#TYPE - 2 :  by using the tertinary operation and recursion.

# def factorial(n):
#     if n < 0:
#         return " the number is not exists"
#     else:
#         # single line to find factorial
#         return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
#
#
# print("Factorial of number is", factorial(5))


# TYPE - 3 : USING THE FOR LOOP .

# def fact_num(n):
#     if n < 0:
#         return " the number is not exist"
#     elif n == 0 or n == 1:
#         return 1
#
#     fact = 1   # this is  local variable
#
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact
#
#
# print(fact_num(5))


#  TYPE - 4 : using the while loop .

# def factorial_num(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         fact = 1
#         while num > 1:
#             fact = fact * num
#             num = num - 1
#         return fact
#
#
# print("factorial of number : ", factorial_num(6))
