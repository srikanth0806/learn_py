"""
   write a programe by using continue in for loop.
"""


def use_brek(li):
    for i in li:
        if i =="srikanth":
            continue
        print(i)


use_brek(["gopi", "harsha", "hari", "srikanth", "sriman", "santosh"])