try:
    fp = open("good")
    fp.read()
except FileNotFoundError:
    print("file is not available")