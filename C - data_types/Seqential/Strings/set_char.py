"""
 write a python programme to separate the 10 char from out of 200 chars,
 and caluclate the duplicate letters.
"""


def separate(s):
    n = len(s)
    print(n)
    li = []

   # di = dict()
    x = 0
    while x < n:
        n = x
        n1 = n + 10
        temp = ""
        for i in range(n, n1):
            temp = temp + s[i]
        li.append(temp)
        x = x + 10

    print(li)
    # print("------------------")
    # for i in s:
    #     if i not in di:
    #         di[i] = 1
    #     else:
    #         di[i] = di[i] + 1
    # print(di)





s = "Welcome Messages: A warm welcome message works like a charm in any" \
    " situation, be it the recruitment of a new employee or having returning" \
    " ones back   "

separate(s)


    #x = 0
    # while x <= 100:
#     print(x)
#     x = x + 10
