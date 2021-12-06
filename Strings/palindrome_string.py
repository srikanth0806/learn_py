"""
7. Define a function is_palindrome()
   that recognizes palindromes

     LOGIC:

        "words that look the same written backwards."
          For example,
                is_palindrome("radar") should return True
     SOLUTION:
         find the reserse of a string  and check
        given string == reserse of a string

          # ** STRING REVERSE **
  #              4 - TYPES
  #        1.BY USING string slicing logic
  #        2.BY USING WHILE LOOP
  #        3.BY USING FOR LOOP
  #        4.BY USING RECURSSION"""


# #1.BY USING STRING SLICING LOGIC:
#
# def is_palindrome(x):
#     print(x)
#     y = x[::-1]
#     print(y)
#     if y == x:
#         return "the string is a  palindrome number"
#     else:
#         return " the string is not palindrome"
#
#print(is_plindrome("srikanth"))



#2.BY USING WHILE LOOP:

# def is_palindrome(s):
#     print(s)
#     s2 = ""   # here, i take an empty string
#     i = len(s)-1
#     while i >= 0:
#         s2 = s2 + s[i]
#         i = i-1
#     print(s2)
#
#     if s == s2:
#         return " the string is palindrome"
#     else:
#         return " the string is not palindrome"
#
#
# print(is_palindrome("srikanth"))


# #  3.BY USING FOR LOOP
#
# def is_palindrome(s):
#     print(s)
#     s2 = ""
#     for i in s:     # absorve the small difference between the bellow two logics.
#      s2 = i + s2       # s2 =s2 + i
#     print(s2)
#
#     if s == s2:
#         return "the string is palindrome"
#     else:
#         return "the string is not palindrome"
#
# print(is_palindrome("srkanth"))





# from Strings.string_reverse import ReverseString


def is_palindrome(s):
    if len(s) >= 0:
        x = s[len(s) - 1] + s[0]

        return is_palindrome(x)

    x = is_palindrome()
    print(x)
    if s == x:
        return "given string is palindrome."
    else:
        return "the string is not palindrome."

# print(is_palindrome("radar"))
print(is_palindrome("srikanth"))

# #  NOTE:
# #      "information  about documentation string."
# # from learn_classes import classmethod
# # print(help(classmethod.Robot.get_robot_count))