"""
   Python program to find uncommon words from two Strings
"""


# type - 1 :

def uncommon(s, s1):
    x = s.split()
    y = s1.split()
    li = []
    for i in x:
        if i not in y:
            li.append(i)
    for i in y:
        if i not in x:
            li.append(i)

    return li

s = "Python program to find uncommon words from two Strings"
s1 = "Reverse words in a given String in Python"

print(uncommon(s, s1))



# type - 2:

# # Python3 program to find a list of uncommon words
#
# # Function to return all uncommon words
# def UncommonWords(A, B):
#     # count will contain all the word counts
#     count = {}
#
#     # insert words of string A to hash
#     for word in A.split():
#         count[word] = count.get(word, 0) + 1
#
#     # insert words of string B to hash
#     for word in B.split():
#         count[word] = count.get(word, 0) + 1
#
#     # return required list of words
#     return [word for word in count if count[word] == 1]


# type - 3:

# # Driver Code
# A = "Geeks for Geeks"
# B = "Learning from Geeks for Geeks"
#
# # Print required answer
# print(UncommonWords(A, B))
#
#
# def uncommon(a,b):
# a=a.split()
# b=b.split()
# k=set(a).symmetric_difference(set(b))
# return k
#
# #Driver code
# if __name__=="__main__":
# a="apple banana mango"
# b="banana fruits mango"
# print(list(uncommon(a,b)))


# type -4 :

# def uncommon(A, B):
# 	un_comm = [i for i in "".join(B).split() if i not in "".join(A).split()]
# 	return un_comm
#
# #Driver code
# A = "Geeks for Geeks"
# B = "Learning from Geeks for Geeks"
# print(uncommon(A, B))

