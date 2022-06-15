try:
    fp = open("test6.txt", "w")
    fp.write("Hello")
    fp.read()
except Exception as e:
    import sys
    #print(sys.exc_info())
    print(type(e).__name__)
    print(e)

finally:
    print(fp.closed)
    fp.close()

    print(fp.closed)

print("good mornign")