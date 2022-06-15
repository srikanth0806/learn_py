"""
   Python program to find second largest number in a list
"""


# Method - 1 ( this is my logic):

def large_ele(li):
    large = li[0]
    second_large = 0
    for i in li:
        if i >= large:
            second_large = large
            large = i
    return second_large


print("the second largest is :", large_ele([23, 45, 67, 12, 77]))


# #Method - 2 :
#
# def largest_ele(li):
#     li.sort()
#     return li[-2]
#
#
# print(" the second largest number in a list is :", largest_ele([23, 45, 56, 20]))



# # Method - 3 : list comprehension
# def secondmax(li):
#     sublist = [x for x in li if x < max(li)]
#     return max(sublist)
#
# if __name__ == '__main__':
#     li = [10, 20, 4, 45, 99]
# print(secondmax(li))



