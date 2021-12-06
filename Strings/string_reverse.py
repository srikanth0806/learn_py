  #              """  ** STRING REVERSE **
  #                           4 - TYPES
  #                        1.BY USING STRING SLICING LOGIC
  #                        2.BY USING WHILE LOOP
  #                        3.BY USING FOR LOOP
  #                        4.BY USING RECURSSION"""


#1.BY USING STRING SLICING LOGIC:

# def reverse(x):
#     y=x[::-1]
#     return y
#
# z=reverse("srikanth")
# print(z)

#2.BY USING WHILE LOOP

# def reverse(s):
    # string2=""
    # i=len(s)-1
    # while i >= 0:
    #     s2=s2+ s[i]
    #     i = i-1
    # print(s2)


#  3.BY USING FOR LOOP

# def reverse(s):
  # s2 = ""
#    for i in x:
#     # absorve the small difference between the bellow two logics.
#     # string2 =string2 + i
#    string2 = i + string2
# print(string2)


#4.BY USING RECURSSION

def ReverseString(s):
    if len(string) == 0:
        return s
    else:
        return ReverseString(string[1:])+string[0]
# if __name__ == "__main__":
#     string=input("enter the string: ")
#     y = ReverseString(string)
#     print(y)









