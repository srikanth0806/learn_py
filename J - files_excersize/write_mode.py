from datetime import datetime

var = open("test3.txt", "w")
var.write("i am srikanth")
var.write(datetime.now().strftime("%d - %m - %Y : %I %M %S"))
var.close()
