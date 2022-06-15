import sys

try:
    x = 10/0

except Exception as e:
    print(e)
    print(type(e).__name__)
    print(sys.exc_info())

