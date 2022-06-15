"""
32.Python Program to Display Fibonacci Sequence Using Recursion

   Fibonacci series:

        A Fibonacci sequence is the integer sequence of
        0, 1, 1, 2, 3, 5, 8.

        n1,n2,n3.........,n.

The first two terms are 0 and 1. All other terms are
 obtained by adding the preceding two terms. This means
to say the nth term is the sum of (n-1)th and (n-2)th term.

      LOGIC:                # just like swap case
            n_term = n1 + n2
            n1 = n2
            n2 = n_term   """


def fib(n):

    if n < 0:
        print("please enter the positive integer:")

    elif n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


for i in range(13):   # number passing one by one .
    print(fib(i))

