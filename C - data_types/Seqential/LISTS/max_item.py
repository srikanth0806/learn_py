#. Write a Python program to get the largest number from a list


def max_items(a):
    max = a[0]
    for i in a:
        if i > max:
            max = i
    return max


print(max_items([56, 87, 12, 130, 34]))
