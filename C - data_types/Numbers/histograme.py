"""
11. Define a procedure histogram()
that takes a list of integers and prints a histogram to the screen.
 For example, histogram([4, 9, 7]) should print the following:
          ****
          *********
          *******    """


def histogram(li):
    for i in li:
        num = 0
        while num < i:
            print("*", end="")
            num = num + 1
        print("\n")


k = histogram([8, 6, 5])
print(k)



def histogram(li):
    for i in li:
        print("*"*i)
