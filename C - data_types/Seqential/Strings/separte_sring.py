"""
 write a python programme to separate the 10 words from out of 200 words,
 and caluclate the duplicate letters.
"""


def separate(s):
    li = s.split()
    n = len(li)
    print(n)
    A = "abcdefghmo"
    di = dict()
    x = 0
    while x < 100:
        n = x
        n1 = n + 10
        for i in A:
            i = []
            for j in range(n, n1):
                i.append(li[j])
        print(i)
        x = x + 10
    print("------------------")
    for i in s:
        if i not in di:
            di[i] = 1
        else:
            di[i] = di[i] + 1
    print(di)





s = "Welcome Messages: A warm welcome message works like a charm in any" \
    " situation, be it the recruitment of a new employee or having returning" \
    " ones back, or meeting friends after a long time! Welcome messages are" \
    " also appreciated in more formal settings like welcoming a guest or " \
    "customer. Whatever the arrangement is, these notes convey your excitement" \
    " and happiness towards the other parties and help them settle in more " \
    "comfortably. So if you have a new party to meet and greet them cordially," \
    " pass along a sweet, meaningful welcome message while offering them a " \
    "genuine smile! Perfect welcome messages can " \



separate(s)