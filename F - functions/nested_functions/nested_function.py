# Python program to illustrate
# nested F - functions
def outerFunction(text):
    word = text

    def innerFunction():
        print(word)
        return 6

    innerFunction()
    return innerFunction



print(outerFunction('Hey!'))