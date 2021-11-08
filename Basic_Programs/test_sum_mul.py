"""5. Define a function sum() and a function multiply()
that sums and multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10,
 and multiply([1, 2, 3, 4]) should return 24."""

def sum(x):
    sum = 0
    for num in x:
        sum=sum+num
    return sum

def mul(x):
    res=1
    for num in x:
        res = res * num
    return res
z=mul((1,2,3,4))
print(z)

# y=sum[1,2,3,4]
# print(y)