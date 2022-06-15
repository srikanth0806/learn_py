#5. Write a Python program to count the number of  palindrome strings  in a given list.


def f_s_same(l):

    for word in l:
        x = word
        i = 1
        s = ""
        while i <= len(x):
            s = s + x[-i]
            i = i + 1

        if x == s:
            print(x)


print(f_s_same(["ars", "jkj", "kmk", "dsa", "mnm"]))
