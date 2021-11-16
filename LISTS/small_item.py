#Write a Python program to get
# the smallest number from a list
def small_element(li):

    small = li[0]
    for i in li:
        if i < small:
            small=i
    return small

print(small_element([156,87,212]))