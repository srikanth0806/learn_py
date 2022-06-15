"""
   Remove multiple elements from a list in Python
"""

# type - 1:
# def mul_ele_rem(li):
#     x = li[::2]
#     print(x)
#
#
# mul_ele_rem([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# type - 2 :
#
# # Python program to remove multiple
# # elements from a list
#
# # creating a list
# list1 = [11, 5, 17, 18, 23, 50]
#
# # removes elements from index 1 to 4
# # i.e. 5, 17, 18, 23 will be deleted
# del list1[1:5]
#
# print(*list1)




# type - 3:

# def mul_ele_rem(li):
#
#    for i in li:
#        if i % 2 == 0:
#            li.remove(i)
#    return li
#
#
# print(mul_ele_rem([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# type - 4 :

# # Python program to remove multiple
# # elements from a list
#
# # creating a list
# list1 = [11, 5, 17, 18, 23, 50]
#
# # will create a new list,
# # excluding all even numbers
# list1 = [ elem for elem in list1 if elem % 2 != 0]
#
# print(*list1)




# type -5 :

# Python program to remove multiple
# elements from a list

# creating a list
list1 = [11, 5, 17, 18, 23, 50]

# given index of elements
# removes 11, 18, 23
unwanted = [0, 3, 4]

for ele in sorted(unwanted, reverse = True):     #--- ardham kala
	del list1[ele]

# printing modified list
print (*list1)
