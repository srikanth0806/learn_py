"""
   write a python programme to separate the sequence into sublist.
"""
li = list(range(100))
temp = []
li_len = len(li)

i = 0
x = 1
j = 1
while i < li_len :
    x = i + j
    print(i, x)
    temp.append(li[i:x])
    i = x
    j += 1

print(temp)














