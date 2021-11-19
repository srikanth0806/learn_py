"""
    Python Program to Convert Decimal to
    Binary, Octal and Hexadecimal.

      logic:
            x = temp % 2
            y = temp //2
            temp = y
 """

def convert(num):

    li = []
    while num > 0:
        x = num % 2
        li.append(x)
        y = num // 2
        num = y
    li.reverse()
    a = str(li)
    #print("the binary value of the given number is :", a)
    return a
print(convert(85))
