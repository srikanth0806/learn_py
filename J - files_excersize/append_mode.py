"""
    write a programme using append mode in a file.
           or
    # Write a Python program
    to append text to a file and display the text.
"""

var = open("test2.txt", "a")
a = var.write("this is compile test\n")
print(a)    # here, write mode prints how many letters you are
b = var.write("i am using  append mode.\n")   # written.
var.close()


# In the above programme,
#I write some message in the a and b variables.
