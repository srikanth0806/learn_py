"""The deque in a collections is used for
to append a element left or right side in a list."""

from collections import deque

x = deque()

x.append(20)
x.append(30)
x.appendleft("srikanth")

print(x)

y = ["gopi","murali",40,4.5]
# y.extend(x)
# print(y)
# x.extendleft(y)
# print(x)
y.reverse()
print(y)
y.sort()
print(y)    # type error raised.



