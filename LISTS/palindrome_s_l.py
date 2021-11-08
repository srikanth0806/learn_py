#5. Write a Python program to count the number of  palindrome strings  in a given list.
def f_s_same(l):
    count=0
    for word in l:
        a=word
        b=a.reverse()
        if a == b:
            print(word)
            count += 1
    return count
print(f_s_same(["ars","jkj","kmk","dsa","mnm"]))