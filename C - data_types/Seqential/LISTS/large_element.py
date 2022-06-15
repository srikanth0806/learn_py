"""
    Python program to find largest number in a list.
"""

# Method - 1 (My logic):


def large_ele(li):
    large = li[0]
    for i in li:
        if i >= large:
            large = i
    return large


print("the large number in list is :", large_ele([23, 130, 45, 20, 65]))



# #Method - 2: Using max() method
#
# # list of numbers
# list1 = [10, 20, 4, 45, 99]
#
# # printing the maximum element
# print("Largest element is:", max(list1))



# Method - 3 : Sort the list in ascending order and print the last element in the list.
#
#
# # Python program to find largest
# # number in a list
#
# # list of numbers
# list1 = [10, 20, 4, 45, 99]
#
# # sorting the list
# list1.sort()
#
# # printing the last element
# print("Largest element is:", list1[-1])


# # Method - 4: Find max list element on inputs provided by user
#
# # creating empty list
# list1 = []
#
# # asking number of elements to put in list
# num = int(input("Enter number of elements in list: "))
#
# # iterating till num to append elements in list
# for i in range(1, num + 1):
#     ele = int(input("Enter elements: "))
#     list1.append(ele)
#
# # print maximum element
# print("Largest element is:", max(list1))
