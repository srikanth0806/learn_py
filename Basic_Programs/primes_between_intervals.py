"""15 Python Program to Print all Prime Numbers
 in an Intervals."""


def prime_number(a, b):

    for num in range(a, b+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)


print(prime_number(23, 56))
print(prime_number(1, -100))
print(prime_number(10, -10))
