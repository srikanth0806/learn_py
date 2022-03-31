"""write a Python Program to check the given number is a Prime Number
 or not.

            LOGIC:
                num % i == 0


# EXPLANATION:
What is the Prime Number?
          A prime number is an integer greater than one
          and can be divisible by one and only itself.

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
        return "the given number is not exist"

    else:
        for i in range(2, num):    # this for is used  to find
            if num % i == 0:       # the factors of num from 2 to num-1.
                return "the given number is not prime"
        else:
            return "the given number is prime"

# 1 and num are also the factors of that number so we consider
#  starting position 2.


print(prime_number(29))
print(prime_number(-100))
print(prime_number(70))


