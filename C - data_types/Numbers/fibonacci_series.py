"""
   18.Python Program to Print the Fibonacci sequence.

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


def fib(n_term):
    if n_term <= 0:
        print("please enter the positive integer:")

    elif n_term == 1:
        print(n_term)

    n1, n2 = 0, 1
    print(n1)
    print(n2)

    for i in range(2, n_term):
        n_term = n1 + n2
        n1 = n2
        n2 = n_term
        # if n_term > 100:   #this condition is used for
        #     break          #fibonacci series under 100.
        print(n_term)


fib(30)
