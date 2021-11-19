#. Write a Python program to sum all the items in a list
def list_sum(items):
    sum=0
    for i in items:
        sum += i
    return sum
print(list_sum([1,2,7]))