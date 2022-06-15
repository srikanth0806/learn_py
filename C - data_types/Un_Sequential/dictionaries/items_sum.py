"""
   Python program to find the sum of all items in a dictionary
"""


# Method - 1: without using any functions.

def sum_items(di):
    sum = 0
    for i in di:
        sum = sum + di[i]

    return sum


di = {1: 23, 2: 45, 3: 56}
print(sum_items(di))




# Method - 2 : with using the values()  and sum() functions.


# def sum_items(di):
#     x = di.values()
#     y = sum(x)
#     return y
#
#
# di = {1: 23, 2: 45, 3: 56}
# print(sum_items(di))


# Method - 3 :


# def returnSum(dict):
# 	return sum(dict.values())
#
#
# # Driver Function
# dict = {'a': 100, 'b': 200, 'c': 300}
# print("Sum :", returnSum(dict))



