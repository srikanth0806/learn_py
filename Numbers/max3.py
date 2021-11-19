"""2. Define a function max() that takes three numbers as arguments and
      returns the largest of them."""
def max_num(a,b,c):
    if a<b:
        if b<c:
            return c
        else:
            return b
    elif a>b:
            return a
x=max_num(40, 75,200)
print(x)


