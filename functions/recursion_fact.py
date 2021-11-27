"""
34.Python Program to Find Factorial of Number Using Recursion

       DEFINITION:
                 The factorial of a number is
                 the product of all the integers
                 from 1 to that number.

        For example,
            the factorial of 6 is 1*2*3*4*5*6 = 720.
           Factorial is not defined for "negative numbers"
                and
           the factorial of zero is one, 0! = 1.

       LOGIC:
            n * func(n-1)
"""


def fact(n):

    if n <= 0:
        return "we cann't find the the factorial of the given number"
    elif n == 1:
        return n
    else:
        return n * fact(n-1)


print(fact(6))
print(fact(0))
print(fact(-6))

