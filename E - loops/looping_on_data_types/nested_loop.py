"""
   write a programe by Nested loop.

    Different types:
                    1.for in for
                    2.for in while
                    3.while in for
                    4.while in while

"""

#1.for in for:

def use_brek(li):

    for i in li:
        if i == "srikanth":
           for char in i:
               print(char,end=" ")


use_brek(["gopi", "harsha", "hari", "srikanth", "sriman", "santosh"])


print("\n")


#2.for in while :

def use_brek(s):

    while s == "hari":
        for i in s:
            print(i, end=" ")
        break

use_brek("hari")


print("\n")


# 1.while in for:

def use_brek(li):
    for i in li:
        while i == "sriman":
            print(i)
            break

use_brek(["gopi", "harsha", "hari", "srikanth", "sriman", "santosh"])


#4.while in while :


