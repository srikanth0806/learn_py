# Write a Python program to multiply all the items in a list
def list_mul(items):
    mul=1
    for i in items:
        mul *= i
    return mul
print(list_mul([1,2,7]))
print(list_mul([1,3,"srikanth"]))
print(list_mul([1,3,[9,7],"srikanth"]))
