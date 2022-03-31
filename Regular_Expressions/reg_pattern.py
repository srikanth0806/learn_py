import re

text = """9848022338For registration	YESREG (from your registered mobile number) send it to 9840909000
For Account balance	YESBAL <customer ID> send it to 9840909000
Block credit Card	BLKCC <space><last 4 digit> send it to 9840909000
Missed call banking For account balance	Number 09223921111"""

text2 = """For registration	YESREG (from your registered mobile number) send it to 9840909000
For account balance	YESBAL <customer ID> send it to +91-9840909000
Block credit card	BLKCC <space><last 4 digit> send it to +91-9840909035
Missed call banking For account balance	Number 09223921111"""

# x = re.search("", text2)
#
# print(type(x.group()), x.group())

x = re.findall("\+(91)-(\d{10})", text2)

#print(x.group(), x.group(1), x.group(2))
print(x)

for i in x:
    print(i[1])