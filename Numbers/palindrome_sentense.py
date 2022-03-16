import string


def palindrome(x):
    temp = ""
    for i in x:
        if i in 'abcdefghijklmnopqrstuvwxyz' \
                or i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            temp += i
    temp = temp.upper()
    print(temp)
    if temp == temp[::-1]:
        return True
    else:
        return False


s = palindrome("Go hang a salami I'm a lasagna hog.")
print(s)