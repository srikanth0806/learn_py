"""
    Python Program to Count the Number of Occurrence of a Character in String
"""


# def count_charecters(s):
#     for i in s:
#         print(s.count(i))
#
#
# count_charecters("srikanthsrk")



def count_charecters(s):
    count = 0
    for i in s:
        for j in s:
            if i == j:
                count += 1
                print(i, " - ", count)
            else:
                print(i,"-", 1)


print(count_charecters("srikanthsrk"))
