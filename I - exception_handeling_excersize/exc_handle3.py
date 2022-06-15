import sys
try:
    fp = open("basics.py")
    fp.write()
except:
    print(sys.exc_info())

else:
    print("else block executed")

finally:
    try:
        fp.close()
        print("file closed successfuly")
        print(fp.closed)
    except NameError:
        print(sys.exc_info())