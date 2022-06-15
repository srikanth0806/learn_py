"""
#     write a python programme to find the
#     sum and average of first n natural numbers.

#       LOGIC:
#             sum = sum + i
#             average = sum /total numbers
"""


def add_average(n):

    sum = 0
    for i in range(0, n+1):
        sum = sum + i

    average = sum / n

    return sum, average


print("the sum and average of n natural numbers are:", add_average(10))


# SOLUTION - 2 :

# n = 20
# formula to calculate sum
# res = n * (n + 1) / 2
# print('sum of first', n, 'numbers is:', res)
# # Output sum of first 20 numbers is: 210.0

# formula to calculate average
# average = (n * (n + 1) / 2) / n
# print('Average of first', n, 'numbers is:', average)
# # Output Average of 20 numbers is: 10.5

# #SOLUTION - 3 :
#
# n = 20
# # formula to calculate sum
# res = n * (n + 1) / 2
# print('sum of first', n, 'numbers is:', res)
# # Output sum of first 20 numbers is: 210.0
#
# # formula to calculate average
# average = (n * (n + 1) / 2) / n
# print('Average of first', n, 'numbers is:', average)
# # Output Average of 20 numbers is: 10.5
#
# #SOLUTION -4 :
#
#
#
# input_string = input('Enter numbers separated by space ')
# print("\n")
# # Take input numbers into list
# numbers = input_string.split()
#
# # convert each item to int type
# for i in range(len(numbers)):
#     # convert each item to int type
#     numbers[i] = int(numbers[i])
#
# # Calculating the sum and average
# print("Sum = ", sum(numbers))
# print("Average = ", sum(numbers) / len(numbers))