
fpw = open("C:\\Users\\sRIKANTH\\Documents\\learn_py\\test_append.txt", 'x')

fpw.write("i am appening to existing file")

fpw.close()

path = "C:\\Users\\sRIKANTH\\Documents\\learn_py\\test_append.txt"
fp = open(path, 'x')
my_data = fp.write("i am writing exiting file")
print(my_data)
fp.close()
