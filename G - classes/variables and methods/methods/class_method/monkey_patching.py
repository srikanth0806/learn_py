def pach_func():
    print("I am patching your functionality")

class A:
    def m(self):
        print("I am method m from class A")

    @classmethod
    def mycls(cls):
        print("i am a cls method")

a = A()
A.mycls()
# a.m()

# a.m = pach_func
A.mycls = pach_func
A.mycls()
