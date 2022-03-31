"""
  27.Python Program to Find LCM.

    DEFINITION OF L.C.M:
        The least common multiple (L.C.M.) of two numbers is
         the smallest positive integer
         that is perfectly divisible by the two given numbers.

  For example,
       the L.C.M. of 12 and 14 is 84.

  LOGIC:
        X % i == 0
        y % i == 0
"""


def l_c_m(a, b):     # THIS IS MY LOGIC

    if a > b:
        big_num = a   # here big_num is used in starting
    else:             # position of range() function.
        big_num = b

    temp = a * b

    for i in range(big_num, temp+1):
        if(i % a == 0) and (i % b == 0):
            x = i
            return x


print("the lcm is :", l_c_m(10, 15))
print("the lcm is :", l_c_m(1, 2))
print("the lcm is :", l_c_m(12, 14))



# ANOTHER WAY - 2 :


# # Python Program to find the L.C.M. of two input number
#
# def compute_lcm(x, y):
#
#    # choose the greater number
#    if x > y:
#        greater = x
#    else:
#        greater = y
#
#    while(True):
#        if((greater % x == 0) and (greater % y == 0)):
#            lcm = greater
#            break
#        greater += 1
#
#    return lcm
#
# num1 = 54
# num2 = 24
#
# print("The L.C.M. is", compute_lcm(num1, num2))


# ANOTHER WAY -3 :


# # Python program to find the L.C.M. of two input number
#
# # This function computes GCD
# def compute_gcd(x, y):
#
#    while(y):
#        x, y = y, x % y
#    return x
#
# # This function computes LCM
# def compute_lcm(x, y):
#    lcm = (x*y)//compute_gcd(x,y)
#    return lcm
#
# num1 = 54
# num2 = 24
#
# print("The L.C.M. is", compute_lcm(num1, num2))



