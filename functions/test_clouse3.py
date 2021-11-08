

def my_func():
    def test():
        print("hello")
    return test

x = my_func()
x()