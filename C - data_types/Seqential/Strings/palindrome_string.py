"""
    Python program to check whether the string is
    Symmetrical or Palindrome
"""

# type - 1 :   Using String slice concept


def pal(s):
    x = s[::-1]
    if s == x :
        return True
    else:
        return False


print(pal("srikanth"))
print(pal("raar"))



# # type - 2 :  using while loop concept
#
# def pal(s):
#     x = ""
#     i = 1
#     n = len(s)
#     while i <= n:
#         x = x + s[-i]
#         i = i + 1
#     if s == x:
#         return "the string is palindrome"
#     else:
#         return "the string is not palindrome"
#
# print(pal("srikanth"))
# print(pal("rar"))



# type - 3 :  Using for loop concept


# def pal(s):
#     rev = ""
#     for i in range(len(s), 0, -1):
#         rev = rev + s[i-1]
#     if s == rev :
#         return  " the string is palindrome"
#     else:
#         return "the string is not palinrome"
#
#
# print(pal("srikanth"))
# print(pal("rar"))





# # type - 4 : reversed() Bultin function


# def pal(s):
#     # joining characters of reversed string one by one
#     reversed_string = ''.join(reversed(s))
#     if reversed_string == s:
#         return "the string is Palindrome"
#     else:
#         return "the string is not Palindrome"
#
#
# print(pal("MALAYALAM"))


   #    or    #

# def pal(s):
#     rev = reversed(s)
#     print(rev)  # reversed function returns one of the object,
#     if list(s) == list(rev):    # so that we can use list function
#         return "the string is palindrome"
#     else:
#         return "the string is not palindrome"
#
#
# print(pal("srikanth"))
# print(pal("rar"))


# type - 5 :

# string = 'amaama'
# half = int(len(string) / 2)
#
# if len(string) % 2 == 0:  # even
#     first_str = string[:half]
#     second_str = string[half:]
# else:  # odd
#     first_str = string[:half]
#     second_str = string[half + 1:]
#
# # symmetric
# if first_str == second_str:
#     print(string, 'string is symmertical')
# else:
#     print(string, 'string is not symmertical')
#
# # palindrome
# if first_str == second_str[::-1]:  # ''.join(reversed(second_str)) [slower]
#     print(string, 'string is palindrome')
# else:
#     print(string, 'string is not palindrome')
