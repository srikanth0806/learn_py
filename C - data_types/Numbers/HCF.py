"""
Python Program to Find HCF or GCD.

  DEFINITION OF H.C.F:
        The Highest Common Factor(HCF) of two numbers is
        the highest possible number which divides
        both the numbers exactly.

        EX:
            HCF of 24 and 36 is 12.

        The highest common factor (HCF) is
        also called the greatest common divisor (GCD)


        LOGIC:
             X % i == 0  and  y % i == 0
"""


def h_c_f(a, b):

    if a < b:
        small_num = a
    else:
        small_num = b

    for i in range(2, small_num):

        if (a % i == 0) and (b % i == 0):
            x = i

    return x


y = h_c_f(16, 24)

print("the heighest common factor of given number is :", y)


# In range function, I doesn't consider the 0 and 1.
# Because,
# if 0 is consider then the  loop will go to infinite.
#1 is always factor of the all positive numbers.
# so it doesn't consider.