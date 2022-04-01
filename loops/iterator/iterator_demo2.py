"""
write a python programme to demonestrte the iterators.
"""

class TopTen:
    def __init__(self):
        self.x = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.x <= 10:
            val = self.x
            self.x += 1
            return val
        else:
            raise StopIteration


tt = TopTen()    # here, tt is an iterator object
#    observe the below statements
print(tt.__next__()) # ----> here,1 is executed

print(next(tt))      # ----->here, 2 is executed

for i in tt:        # -----> here, 3 to 10 are executed
    print(i)
