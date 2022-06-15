"""
   Python Program to Randomly Select an Element From the List
"""
import random


def element_randm(li):
    for i in random.choices(li):
        print(i)


element_randm([23, 67, 89, 67, 45, 32, "srikanth"])
element_randm([23, 67, 89, 67, 45, 32, "srikanth"])

