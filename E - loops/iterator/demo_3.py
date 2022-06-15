"""
   write a python programme on iterator.
"""


class Myiterator():
    def __init__(self):
        self.x = 1

    # when we initialize the values in __iter__() method,
    # the for loop reexcute this method. shown below
    def __iter__(self):
        #self.x = 1
        return self

    def __next__(self):
        if self.x <= 10:
            val = self.x
            self.x = self.x + 1
            return val
        else:
            raise StopIteration


mi = Myiterator()

# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))

print(mi.__next__())
print(mi.__next__())
print(mi.__next__())
print(mi.__next__())

print("----------")

for i in mi:
    print(i)
