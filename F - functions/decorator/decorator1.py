
def my_decorator(func):
    def my_closure():
        print("i  got  decorated")
        func()
    return my_closure

@my_decorator
def myfunc():
    print("i am not  decorated now")

#decorator = my_decorator(myfunc)
#decorator()

myfunc()