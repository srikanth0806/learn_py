with open("test.txt", "r+") as f:
    data = f.readlines()
    for line in data[0::2]:
        word = line.split()
        print(word)
