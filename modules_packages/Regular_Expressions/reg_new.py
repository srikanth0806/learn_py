import re

text = """9848022338For registration	YESREG (from your registered mobile number) send it to 9840909000
For Account balance	YESBAL <customer ID> send it to 9840909000
Block credit Card	BLKCC <space><last 4 digit> send it to 9840909000
Missed call banking For account balance	Number 09223921111"""

text2 = """For registration	YESREG (from your registered mobile number) send it to 9840909000
For account balance	YESBAL <customer ID> send it to 9840909000
Block credit card	BLKCC <space><last 4 digit> send it to 9840909000
Missed call banking For account balance	Number 09223921111"""

"""
compile

match   #must use  gropu() for output , if no match return None
search  # same as abovve

findall # return list of matched occurances of no match empty list
sub     # return a string with substitution of a string what we have given
"""
#x = re.compile("pattern")

# res = re.search("0?\d{10}", text)
# print(res)
# final_output = res.group()
#
# print(res)
# print(final_output)

# res = re.match("\d{10}", text)
# if res:
#     final_output = res.group()
#     print(res)
#     print(final_output)

res = re.findall("\d{10,11}", text)
print(res)


# val = x.sub("MOBILE NUMBER", text, 2)
# print(val)
