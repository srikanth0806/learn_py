"""
    Python Program to Find Sum of Natural Numbers
    Using Recursion.

    DEFINITION:
             Natural numbers are countable numbers,
             including:
                      only the positive integers
                      i.e. 1, 2, 3, 4,5,6, ……….
             excluding:
              zero, fractions, decimals and negative numbers.

   LOGIC:
      sum = 1+2+3..............n """


def total(n):

    if n <= 0:
        return "given number is not natural."
    elif n == 1:
        return n
    else:
        return n + total(n-1)


print(total(5))
# print(total(-3))
# print(total(0))
# print(total(25))