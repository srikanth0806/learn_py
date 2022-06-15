var = open("test2.txt", "r")
var.seek(30)
print(var.tell())
print(var.readlines())
var.close()

