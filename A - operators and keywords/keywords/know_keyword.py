""" checking given word is keyword  or not

    Note:
         importing "keyword" for keyword operations
         use  iskeyword() method.
"""


import keyword


def know_keyword(k):
    if keyword.iskeyword(k):
        return (k + " is python keyword")
    else:
        return (k + " is not a python keyword")


print(know_keyword("for"))
print(know_keyword("hai"))

