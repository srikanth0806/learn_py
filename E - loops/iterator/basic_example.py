"""
    write a python programme to print the values one by one
    with using the iterator.
"""


class BasicIterator:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = BasicIterator()  # here values is an iterator object
print(next(values))      #here, notice one point. the for taken values from 2 .
                         # because one time next method is executed.
for i in values:
    print(i)


