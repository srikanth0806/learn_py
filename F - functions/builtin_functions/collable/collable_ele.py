"""
 write a python programme to perform the collable() function.

definition:
    In general, a callable is something that can be called.
    This built-in method in Python checks and returns True
    if the object passed appears to be callable,
    but may not be, otherwise False.

Syntax:
    callable(object)

    The callable() method takes only one argument,
     an object and returns one of the two values:

    returns True, if the object appears to be callable.
    returns False, if the object is not callable.

Note:
    There may be few cases where callable() returns true,
     but the call to object fails.
     But if a case returns False, calling object will never succeed."""


#Case : When Object is callable


# Python program to illustrate
# callable()
# a test function
def Geek():
    return 5

# an object is created of Geek()
let = Geek
print(callable(let))

# a test variable
num = 5 * 5
print(callable(num))


"""Output:
    True
    False """

"""
    Explanation:

        Here, we see in the first case when an object is passed 
        in the callable() method, it returns True. 
        It is so because let is an object to
        the callable function Geek (which may not be in all cases).

        In the second case num is absolutely not a callable object,
        so the result is False.
        
        The built-in callable() method checks if the argument 
        is either of the two:
                An instance of a class with a __call__ method.
                Is of a type that has a which indicates callability
                 such as in functions, methods etc. 
                 or has a non null tp_call (c struct) member """



# Example:


# Python program to illustrate
# callable()
class Geek:
    def __call__(self):
        print('Hello GeeksforGeeks')

# Suggests that the Geek class is callable
print(callable(Geek))

# This proves that class is callable
GeekObject = Geek()
GeekObject()


"""
Output:
True
Hello GeeksforGeeks  """

"""
Explanation: Since the first case returns and prints True, 
it suggests that the class Geek may be callable.
 Following this, we are able to call the __call__ method and 
 it is accessible, thus proving the class is callable."""

#Case : When Object is NOT callable

#Let’s see what happens in this example:


# Python program to illustrate
# callable()
class Geek:
  def testFunc(self):
    print('Hello GeeksforGeeks')

# Suggests that the Geek class is callable
print(callable(Geek))

GeekObject = Geek()
# The object will be created but
# returns an error on calling
GeekObject()

"""
Output:

True """

"""
Explanation: 
    The callable() method returns True suggesting that 
    the Geek class is callable, but the instance of Geek is not callable()
     and it returns a runtime error:

    Traceback (most recent call last):
      File "/home/3979dc83032f2d29befe45b6ee6001a4.py", line 10, in 
        GeekObject()
    TypeError: 'Geek' object is not callable """
    