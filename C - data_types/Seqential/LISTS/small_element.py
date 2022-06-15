#Write a Python program to get
# the smallest or minimum number from a list

# type - 1 (My logic):

def small_element(li):

    small = li[0]
    for i in li:
        if i < small:
            small = i
    return small


print(small_element([156, 87, 212]))



# # Method - 2: Using min() method
#
# list1 = [10, 20, 1, 45, 99]
# print("Smallest element is:", min(list1))
#
#
#
# #Method - 3: Sort the list in ascending order and print the first
# # element in the list.
#
#
# list1 = [10, 20, 4, 45, 99]
# list1.sort()
# print("Smallest element is:", *list1[:1])
#
#
#
# #Method -4: Find min list element on inputs provided by user.
#
# list1 = []
# num = int(input("Enter number of elements in list: "))
# for i in range(1, num + 1):
#     ele = int(input("Enter elements: "))
#     list1.append(ele)
# print("Smallest element is:", min(list1))

