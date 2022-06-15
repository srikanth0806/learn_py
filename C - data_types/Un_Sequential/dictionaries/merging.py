"""
   Python | Merging two Dictionaries
"""


def merge_di(di1, di2):
    di1.update(di2)       #  don't write -----> x = di1.update(di2)
    return di1


di1 = {"name": "srikanth", "age": 28}
di2 = {"designation": "software", "village": "75 tyallur"}
print(merge_di(di1, di2))
