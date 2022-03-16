"""Print characters from a string
that are present at an even index number .

   LOGIC:
         by using the string slicing."""


def even(s):

    x = s[::2]
    return x


print("the strings are:", even("srikanth"))


#    ANOTHER WAY:

# def evens(s):
#
#     x = len(s)
#
#     for n in range(0, x-1, 2):
#         print(s[n], end="")


#print(evens("srikanth"))
