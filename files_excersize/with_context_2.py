try:
    with open("test4.txt", 'x') as fp:
        print(fp.write("good"))
except FileExistsError:
    print("file alreay present use append mode")