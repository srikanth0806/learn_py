import sys
try:
    r = 2 + "srikanth"
    print(r)
except TypeError as e:
    print(e)
    print(type(e).__name__)
    print(sys.exc_info())

