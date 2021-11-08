
#7. Define a function is_palindrome() that recognizes palindromes
"""NOTE:
     LOGIC:

        "words that look the same written backwards."
          For example,
                is_palindrome("radar") should return True
     SOLUTION:
         find the reserse of a string  and check
        given string == reserse of a string

          # ** STRING REVERSE **
  #              4 - TYPES
  #        1.BY USING FUNCTION
  #        2.BY USING WHILE LOOP
  #        3.BY USING FOR LOOP
  #        4.BY USING RECURSSION"""
#
from basic_programes1.string_reverse import ReverseString
def is_palindrome(x):
    string2=ReverseString(x)
    if x==string2:
        print("given string is palindrome.")
    else:
        print("the string is not palindrome.")

is_palindrome("radar")
is_palindrome("srikanth")

#  NOTE:
#      "information  about documentation string."
# from learn_classes import classmethod
# print(help(classmethod.Robot.get_robot_count))