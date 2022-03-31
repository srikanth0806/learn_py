# Write a Python program to append text to a file and display the text.
fp = open("test2.txt", "a")
x = fp.append("srikanth is a good boy")
print(x)
fp.close()
