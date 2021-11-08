"""
12. The function max() from exercise 1) and the function max_of_three()
from exercise 2) will only work for two and three numbers, respectively.
But suppose we have a much larger number of numbers, or
Suppose we cannot tell in advance how many they are?
Write a function max_in_list()
that takes a list of numbers and returns the largest one."""

def max_in_list(li):
    heigst_num=li[1]
    for i in li:
        if i>heigst_num:
              heigst_num=i
    return heigst_num


k=max_in_list([4,34,56,78,90,2,45,6])
print(k)
