def outerfunction (text):


    def innerfunction():

        print(text)
    return innerfunction

a = outerfunction("Hello")
a()

print(a)