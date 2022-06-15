"""
    write a python programme to find the duplicate elements with index numbers.
"""


def duplicates(li):
    # dup = []
    # for i, j in enumerate(li):
    #     if j not in dup:
    #         dup.append(j)
    #     else:
    #         print("index=%d, value = %d" %(i, j))
    for i, j in enumerate(li):
        if li.count(j) > 1:
            print("value = %d, index = %d " %(j, i))


duplicates([1, 4, 5, 6, 5, 2, 4, 4])
