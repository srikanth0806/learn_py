"""
    Python program to find N largest elements from a list

    # simple logic:
# li = [23, 5, 67, 89, 34, 67, 56, 32, 46]
# n = 4
# li.sort()
# print(li[-n:])
"""

# Method - 1 (using for and sort):

# def large_n_numbers(li, n):
#     li.sort()
#     for i in range(1, n+1):
#         print(li[-i])
#
#
# large_n_numbers([23, 5, 67, 89, 34, 67, 56, 32, 46], 4)

# Method - 2 (using while and sort() method)

# def large_n_numbers(li, n):
#     li.sort()
#     i = 1
#     while i <= n:
#         print(li[-i])
#         i = i + 1
#
#
# large_n_numbers([23, 5, 67, 89, 34, 67, 56, 32, 46], 4)


# Note:

# Method - 2 (using while and sort() method)
#
# def large_n_numbers(li, n):
#     li.sort()
#     i = -4
#     while i <= -1:
#         print(li[i])
#         i = i + 1
#
#
# large_n_numbers([23, 5, 67, 89, 34, 67, 56, 32, 46], 4)


# Mehtod - 3:


def max_n_elements(li, n):
    temp = []

    for i in range(0, n):
        large = li[0]
        for j in li:
            if j >= large:
                large = j

        temp.append(large)
        li.remove(large)
    print(li)
    return temp


li = [2, 6, 41, 85, 0, 3, 7, 6, 10]
n = 3
print(max_n_elements(li, n))
