"""
    Python program to print even numbers in a list
"""


# Method - 1 :
# finding the evens in a list by using the for loop.

def even_elements(li):
    temp =[]
    for i in li:
        if i % 2 == 0:
            temp.append(i)
    return temp


print(even_elements([1, 2, 3, 5, 78, 9, 6, 8, 4]))



# Method - 2 :
# finding the evens in a list by using the while loop.

def even_elements(li):
    temp =[]
    i = 0
    while i < len(li):
        if li[i] % 2 == 0:
            temp.append(li[i])
        i = i + 1

    return temp


print(even_elements([1, 2, 3, 5, 78, 9, 6, 8, 4]))


# Method - 3 : using list comprehension


list1 = [10, 21, 4, 45, 66, 93]
even_nos = [num for num in list1 if num % 2 == 0]

print("Even numbers in the list: ", even_nos)



# Method - 4 : we can also print even no's using lambda exp.

list1 = [10, 21, 4, 45, 66, 93, 11]
even_nos = list(filter(lambda x: (x % 2 == 0), list1))

print("Even numbers in the list: ", even_nos)
