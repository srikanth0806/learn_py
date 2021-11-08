fp = open("test5.txt", "r")
a = fp.read()
print(a)
def r_key_text(var):
    counts = dict()
    mywards=var.split()
    print(mywards)
    for i in mywards:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
mywords_count=r_key_text(a)
print(mywords_count)

