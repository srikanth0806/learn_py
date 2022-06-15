# #step - 1 (pass by value) :-
#
#
# def pass_args(x):
#     x = 8
#     print(x)
#
#
# pass_args(10)


# step -2 (pass by address) :-

def pass_args(x):
    x = 8
    print(x)

a=10
pass_args(a)
print(a)