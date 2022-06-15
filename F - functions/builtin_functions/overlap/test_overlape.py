"""
9. Define a function overlapping() that takes two lists
and returns True if they have at least one member in common, False otherwise.

You may use your is_member() function, or the in operator,
but for the sake of the exercise,

you should (also) write it using two nested for-E - loops."""

         # this is also an example of "nested for loop".

def overlaping(x,y):

    for i in x:
        for j in y:
            if i==j:
                return True

    return False

k=overlaping([1,2,3,4,5,6],["gopi",2,"srikanth"])
print(k)

                

