"""
write a programme to find the second largest number in list
      logic:
         i.by using only logic
         ii.by using sort method in list
         iii.by using set data type , max and remove methods
"""

# TYPE - 1 :

#
# def second_max(li):
#
#     large = max(li[0], li[1])
#     second_large = min(li[0], li[1])
#     n = len(li)
#     for i in range(2, n):
#         if li[i] > large:
#             second_large = large
#             large = li[i]
#
#         # elif li[i] > second_large and  large != li[i]:
#         #     second_large=li[i]
#
#     return second_large
#
#
# print(second_max([213, 56, 9, 456, 65, 525, 600, 289]))


#  METHOD -2:
#           by using sort method

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the second last element
print("Second largest element is:", list1[-2])


#                 (OR)

# Method - 2A:
#         Find max list element on inputs provided by the user

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

# # sort the list
# list1.sort()
#
# # print second maximum element
# print("Second largest element is:", list1[-2])
#
# '''
#
# # print second maximum element using sorted() method
# print("Second largest element is:", sorted(list1)[-2])
#
# Method -3:
#
# By removing the max element from the list
#
# # list of numbers
# list1 = [10, 20, 4, 45, 99]
#
# # new_list is a set of list1
# new_list = set(list1)
#
# # removing the largest element from temp list
# new_list.remove(max(new_list))
#
# # elements in original list are not changed
# # print(list1)
#
# print(max(new_list))
#

#
# Method - 4:
#     Traverse once to find the largest and then once again
#     to find the second largest.
#
#
#
# def findLargest(li):
#     secondLargest = li[0]
#     largest = li[0]
#     for i in range(len(li)):
#         if li[i] > largest:
#             largest = li[i]
#
#     for i in range(len(li)):
#         if li[i] > secondLargest and li[i] != largest:
#             secondLargest = li[i]
#
#     return secondLargest
#
#
# print(findLargest([10, 20, 4, 45, 99]))









