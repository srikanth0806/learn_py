"""
   Python | Ways to remove a key from dictionary
"""


def remove_key(di):
    di.pop("r")
    return di


print(remove_key({"s": 23, "r": 56, "i": 89, "k": 78}))
