"""
36.Python Program to Convert Decimal to Binary Using Recursion


"""


def convertion(n):

    if n > 1:
        convertion(n//2)
        print(n % 2, end=" ")


print(convertion(85))