path = r"C:\Users\sRIKANTH\Desktop\my_test.txt"
path2 = "C:\\Users\\sRIKANTH\\Desktop\\my_test.txt"
fp = open(path, "r")
my_data = fp.read()
fp.close()
fp.seek()
print(my_data)

#====================================

fpw = open("C:\\Users\\sRIKANTH\\Desktop\\test_append.txt", 'x')

fpw.write("i am appening to existing file")

fpw.close()

path = r"C:\Users\sRIKANTH\Desktop\my_test.txt"
fp = open(path, 'x')
my_data = fp.write("i am writing exiting file")
print(my_data)
fp.close()
