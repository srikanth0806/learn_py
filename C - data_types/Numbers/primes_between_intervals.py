#.15 Python Program to Print all Prime Numbers
# in an Intervals.

def prime_number(a, b):

#if a or b <= 1:
    #     return "the given pair is not exist"
# NOTE:
    """ the above code is wrong because
        the range function,
        starts from 0 and increases 1 by default."""

    for j in range(a, b):
        num = j
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#print(prime_number(23,56))
print(prime_number(1, 100))

