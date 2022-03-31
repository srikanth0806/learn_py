import sys
def myfunc():
    myfunc()


try:
    myfunc()
except Exception as e:
    print("exception handled")
    print(e)
    #print(type(e).__name__)
    print(sys.exc_info()[0])
