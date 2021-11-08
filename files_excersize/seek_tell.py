a=open("test2.txt","r")
a.seek(30)
print(a.tell())
print(a.readlines())
a.close()

