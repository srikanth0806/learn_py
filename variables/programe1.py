"""
    difference between the global and local variables."""

#
# def f():
#
#     x = 20
#     print("the value of x is :", x)
# f()
# print(x) # error is raised because the scope of the variable
#          #  is only inside  of the function. but you are clling
#          # out side of the function.



# ANOTHER PROBLEM :

x = 20


def f():

    x = 30
    print("the value of x is:", x)


f()

print("the value of x is :", x)
