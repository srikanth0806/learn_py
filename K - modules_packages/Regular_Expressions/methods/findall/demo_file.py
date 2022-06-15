import re

text = """or 	YESREG (from your  mobile number) send it to 9840909000
For Account balance	YESBAL <customer ID> send it to 09840909000
Block credit Card	BLKCC <space><last 4 digit> send it  to 9840909000 
Missed call banking For account balance srikant srikanthhh Number 9223921111 reg2389"""

y = re.findall("0?", text)
print(y)
y = re.findall("0*", text)
print(y)
y = re.findall("0+", text)
print(y)


y = re.findall("\d", text)
print(y)

y = re.findall("0?\d", text)
print(y)

y = re.findall("0*\d", text)
print(y)

y = re.findall("0+\d", text)
print(y)

y = re.findall("0\d", text)
print(y)
y = re.findall("1?", text)
print(y)
y = re.findall("\d+" , text)
print(y)
y = re.findall("\d*" , text)
print(y)
y = re.findall("\d{2 , 5}" , text)
print(y)
y = re.findall("\d{, }" , text)
print(y)
# y = re.findall("\d{10}" , text)
# print(y)
# y = re.findall("\d{2}" , text)
# print(y)
# y = re.findall("\d{30}" , text)
# print(y)
# y = re.findall("\d{1}" , text)
# print(y)
y = re.findall("[a-z]+" , text)
print(y)
y = re.findall("[a-z]*" , text)
print(y)