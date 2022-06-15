#. Write a Python program to sum all the items in a list

# type - 1 (this is my way):


def list_sum(items):
    sum = 0
    for i in items:
        sum += i
    return sum


print(list_sum([1, 2, 7]))


# type - 2 :  simple way

# # creating a list
# list1 = [11, 5, 17, 18, 23]
#
# # using sum() function
# total = sum(list1)
#
# # printing total value
# print("Sum of all elements in given list: ", total)




# type - 3 :


# total = 0
#
# # creating a list
# list1 = [11, 5, 17, 18, 23]
#
# # Iterate each element in list
# # and add them in variable total
# for ele in range(0, len(list1)):
# 	total = total + list1[ele]
#
# # printing total value
# print("Sum of all elements in given list: ", total)


# type - 4 :

# # Python program to find sum of elements in list
# total = 0
# ele = 0
#
# # creating a list
# list1 = [11, 5, 17, 18, 23]
#
# # Iterate each element in list
# # and add them in variable total
# while (ele < len(list1)):
#     total = total + list1[ele]
#     ele += 1
#
# # printing total value
# print("Sum of all elements in given list: ", total)


# type - 5 :

# # Python program to find sum of all
# # elements in list using recursion
#
# # creating a list
# list1 = [11, 5, 17, 18, 23]
#
# # creating sum_list function
# def sumOfList(list, size):
# if (size == 0):
# 	return 0
# else:
# 	return list[size - 1] + sumOfList(list, size - 1)
#
# # Driver code
# total = sumOfList(list1, len(list1))
#
# print("Sum of all elements in given list: ", total)






