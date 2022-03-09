# 14.Python Program to Check Prime Number.

"""    LOGIC:
             num % i == 0


# EXPLANATION:
What is the Prime Number?
          A prime number is an integer greater than one
          and can be divisible by only itself and one
          i.e it has only two factors.
    NOTE:
          one and numbers less than one
          are not considered as prime numbers.
          (0,-1,-2,-100...etc)

          The smallest prime number is 2 because
          it is divisible by itself and 1 only.

     NOTE:
           A number having more than two factors are
          referred to as composite numbers."""

# coding start:

def prime_number(num):

    if num <= 1:
        return "the given number is not prime"
    elif num > 1 :
        for i in range(2, num): # this for is used  to find
            if num % i == 0:  # the factors of num from 2 to num-1.
                return "the given number is not prime"
                break         # 1 and num are also the factors of that
                              #number so we consider starting position 2.

        else:
             return "the given number is  prime"
#print(prime_number(25))
#print(prime_number(19))
# print(prime_number(0))
# print(prime_number(1))
# print(prime_number(-1))
# print(prime_number(2))
print(prime_number(67))