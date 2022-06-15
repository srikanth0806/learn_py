"""
   Python program to print odd numbers in a List
"""


# Method - 1 : by using the for loop

def odd_elements(li):
    temp = []
    for i in li:
        if i % 2 != 0:
            temp.append(i)

    return temp


print(odd_elements([1, 2, 3, 4, 6, 87, 89, 44]))



# Method - 2: By using the while loop.


def odd_elements(li):
    temp =[]
    i = 0
    while i < len(li):
        if li[i] % 2 != 0:
            temp.append(li[i])
        i = i + 1
    return temp


print(odd_elements([1, 2, 3, 4, 6, 87, 89, 44, 45]))




# Method - 3 : list coprihenssion

def odd_elements(li):
    x = [i for i in li if i % 2 != 0]
    return x


print(odd_elements([1, 2, 3, 4, 6, 87, 89, 44, 45]))



# Method - 4 : using the lambda and filter functions


def odd_elements(li):
    x = filter(lamda i :( i % 2 != 0), li)
    return x
print(odd_elements([1, 2, 3, 4, 6, 87, 89, 44, 45]))
