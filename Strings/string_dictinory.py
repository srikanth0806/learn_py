"""
   write a programme to find the string
   and number of occurances in dictionary format. """


x = "i am sirkanth"
li = x.split()
print(li)
y = dict()

def string_dictinory():

    for i in li:
        if i in y:
            y[i] += 1
        else:
            y[i] = 1
    return y


print(string_dictinory())

