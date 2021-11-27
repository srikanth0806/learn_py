def tree():
    with open("test7.txt", "r+") as f:
        data = f.read()
        words = data.split()
        print(words.count("What"))
        x = dict()
        for i in words:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
    return x


print(tree())


