import copy

x = [1,2,[7,8]]

y = copy.copy(x)

print(y)
y[2][0] = 100
print(y)
print(x)



