"""
   21.Python Program to Find the Sum of Natural Numbers.
      LOGIC:
            sum= sum + i      """


def total():

    sum = 0
    for num in range(1, 10):
        sum = sum + num
    return sum


print("the sum of n natural numbers :", total())