"""Python Program Read a File Line by Line Into a List"""
f = open("test.txt", "r+")
s = str(f)
y = s.splitlines()
print(y)