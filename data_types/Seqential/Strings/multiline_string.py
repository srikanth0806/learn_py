"""
   Python Program to Create a Long Multiline String
"""


def multiline():
    # i placed the \n before the lines
    s = "These are short, famous texts in English from classic sources like " \
        "the Bible or Shakespeare.\n Some texts have word definitions and " \
        "explanations to help you. \n Some of these texts are written in an " \
        "old style of English. \n Try to understand them, because the English " \
        "that we speak today is based on what our great, great, great," \
        "great grandparents spoke before! Of course, not all these texts " \
        "were originally written in English. \n The Bible, for example, " \
        "is a translation.\n But they are all well known in English today, " \
        "and many of them express beautiful thoughts."
    return s


print(multiline())
