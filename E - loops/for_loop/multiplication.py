"""
multiplication table
"""


def multi(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i,"*",j, "=", i * j)
        print("\n")


multi(20)
