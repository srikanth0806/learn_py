#. Write a Python program to get the largest number from a list


def max_items(li):
    max = 0
    for i in li:
        if i > max:
            max = i
    return max


print(max_items([56, 87, 12, 30, 4]))
