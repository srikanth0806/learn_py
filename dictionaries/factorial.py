"""
Python Program for factorial of a number.
factorial = n!, n * n-1 * n-2......*1
 there is a 3-types of code available in python
"""

# TYPE - 1 :

def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
num = 5
print("Factorial of", num, "is",
      factorial(num))


#  TYPE - 2 :

# x="srikanth"

# def factorial_num(num):
#     """this is my doc"""
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
# factorial_num(6)
# # print("factorial of number : ", factorial_num(6))


