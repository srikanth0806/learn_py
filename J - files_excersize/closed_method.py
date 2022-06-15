"""
   write a programme to use closed() method in a file.
"""

fp = open("test6.txt", "w")
fp.write("Hello")

print(fp.closed)
fp.close()

print(fp.closed)

print("good mornign")