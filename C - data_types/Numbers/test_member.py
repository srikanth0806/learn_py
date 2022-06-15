"""8. Write a function is_member() that takes a value
(i.e. a number, string, etc) x and a list of values a,
 and returns True if x is a member of a, False otherwise.
 (Note that this is exactly what the in operator does, but
 for the sake of the exercise you should pretend Python did not have
 this operator.)"""
# def is_member(x,a):
#     if x in a:
#         return True
#     else:
#         return False
# k=is_member("srikanth",[1,2,3,4,5,6,"srikanth"])
# print(k)


def is_member(x, a):
    for i in a:
        if i == x:
            return True
    return False


k = is_member("srikanth", [1, 2, 3, 4, 5, 6, "srikanth"])
print(k)
