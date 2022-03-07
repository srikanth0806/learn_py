"""
 Python Program to Find the Factors of a Number.

 DEFINITION:
           the number, which is divisible by the belowed numbers.
           that all numbers are called as factors of the given number.
       LOGIC:
            num % i == 0
"""


def fact(num):

    for i in range(1, num):

        if num % i == 0:

            print(i)


fact(30)
