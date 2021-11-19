def mul(x, y):
    return x * y
li = [50,51, 52, 53, 54, 55]
li2 = [1, 2, 3, 4,5]
mul_values = list(map(mul,li,li2))
print(mul_values)

mul_values1= list(map(lambda x,y: x * y,li,li2))
res=mul_values1
print(mul_values1)
