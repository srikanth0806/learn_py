def tree(x, y):
    try:
        print("resource opend")
        print(x/y)

    except Exception as e:
        print("Hey, somthing went wrong... that is -", e) # here e denotes exception
    finally:                     #finally block  is always exectes
        print("resource closed") # it is more used in files


tree(20, 5)
tree(20, 0)
tree(20, "s")