import re

text = """or YESREG (from your  mobile number) send it to 9840909000
For Account balance	YESBAL <customer ID> send it to 9840909000
Block credit Card	BLKCC <space><last 4 digit> send it  to 9840909000 
Missed call banking For account balance srikant srikanthhh Number 9223921111 reg2389"""
y = re.search("srikanth?", text)
print(y.group())
print(y.groups())

y = re.search("srikant*",text)
print(y.group())

y = re.search("srikanth+",text)
print(y.group())

#Note:

# ? --> Question mark, matches 1 or 0 character in front of the question mark.
# For example, the below regular expression matches apple and apples.
#
#  regex  is  ----->   apples?


# * --> Astrick, matches 0 or more character in front of the Astrick.
# For example, the below regular expression matches apple,apples,appless,
# aplesssssss (many s ).
#
#  regex  is  ----->   apples*


# + --> plus, matches 1 or more character in front of the plus.
# For example, the below regular expression matches apples and applesssss (many s).
#
#  regex  is  ----->   apples+

y = re.search("[a-z]*" , text)
print(y.group())
#print(y.groups())

# y = re.search("reg\d{4}$", text)
# print(y.group())