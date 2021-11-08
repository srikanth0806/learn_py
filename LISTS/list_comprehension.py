x = list(range(1, 21))

# res = [i**2 for i in x if i % 2 == 0]
# print(res)

#temp = list()
temp = []
for i in x:
    if i % 2 == 0:
        temp.append(i ** 2)
print(temp)

