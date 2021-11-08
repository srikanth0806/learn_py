#Write a Python program to get the smallest number from a list
def max_items(a):
    max = a[0]
    for i in a:
        if i > max:
            max=i
    return i
print(max_items([56,87,12]))