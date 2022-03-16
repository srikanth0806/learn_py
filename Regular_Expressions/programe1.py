"""1. Write a Python program to check that a string contains only a
certain set of characters (in this case a-z, A-Z and 0-9)."""
import re
text = """In123 publishing and graphic design, Lorem123 Ipsum is Placeholder 
        text commonly used to demon78strate the Visual form of a document 
        or a typeface without relying on meaningful content."""
x = re.search("\w*", text)
print(x.group())
y = re.findall("[A-Za-z]+[0-9]+", text)
print(y)

