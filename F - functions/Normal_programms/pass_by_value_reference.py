x = [9,8,7]
y = [1,2,3]

def func(a , b):
    a[0] = 10
    b[0] = 20

print("before func call", x, y)
# 10 8 7, 20 2 3
func(x,y)
print("after func call", x, y)
# 9 8 7, 1 2 3
