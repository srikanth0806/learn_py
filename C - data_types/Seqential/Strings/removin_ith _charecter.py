# Python code to demonstrate
# method to remove i'th character
# using slice + concatenation


# type -1:

def remove_ith(s, ith_char):
    x = ""
    for i in s:
        if i == s[ith_char]:
            continue
        else:
            x = x + i

    return x


print(remove_ith("srikanth python automation", 4))



# type - 2 :

# # Python3 program for removing i-th
# # indexed character from a string
#
# # Removes character at index i
# def remove(string, i):
#     # Characters before the i-th indexed
#     # is stored in a variable a
#     a = string[: i]
#
#     # Characters after the nth indexed
#     # is stored in a variable b
#     b = string[i + 1:]
#
#     # Returning string after removing
#     # nth indexed character.
#     return a + b
#
#
# # Driver Code
# if __name__ == '__main__':
#     string = "geeksFORgeeks"
#
#     # Remove nth index element
#     i = 5
#
#     # Print the new string
#     print(remove(string, i))