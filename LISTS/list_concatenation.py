""""
     write a Python Program to Concatenate Two Lists
"""
# x = [1,2,3]
# y = [6,7,8]
# def concat_list(li, li1):
#     li.extend(li1)
#     return li
#
#
# print(concat_list(x,y))
# print(x,y)

def concat_list(li, li1):
    temp = []
    for i, j in zip(li, li1):    # here, in this zipping is tuple
        temp.append(i)
        temp.append(j)
    return temp


print(concat_list([1, 2, 3, 4, 5], ["srikanth", "gopi", "kumar"]))

