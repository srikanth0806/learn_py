"""1. Write a Python program to check that a string contains only a
certain set of characters (in this case a-z, A-Z and 0-9)."""
import re
text = """In123 publishing and graphic design, Lorem123 Ipsum is Placeholder 
        text commonly used to demonstrate the Visual form of a document 
        or a typeface without relying on meaningful content."""
x=re.search("[a-zA-Z0-9]*", text)
print(x.group())

