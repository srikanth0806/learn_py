"""
    Python program to find Cumulative sum of a list
"""


# def cumulative_sum(li):
#     li1 = []
#     sum = 0
#     for i in li:
#         sum = sum + i
#         li1.append(sum)
#     return li1
#
#
# print(cumulative_sum([10, 20, 30, 40, 50, 60]))



# type - 2 : ardam kala

# Python code to get the Cumulative sum of a list
def Cumulative(lists):
	cu_list = []
	length = len(lists)
    #print(length)
	cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
	return cu_list[1:]

# Driver Code
lists = [10, 20, 30, 40, 50]
print (Cumulative(lists))
