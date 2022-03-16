"""Python Program to Catch Multiple Exceptions in One Line
In this example, you will learn to catch multiple Python exceptions in one line."""

# To understand this example, you should have the knowledge of the following Python programming topics:
#
# Python Input, Output and Import
# Python Errors and Built-in Exceptions
# Python Exception Handling Using try, except and finally statement
# Multiple exceptions can be caught using a tuple. The errors can be passed through a tuple as shown in example below.
#
# Multiple exceptions as a parenthesized tuple


def exp_multi_line(s):
    try:
         print(string + num)
    except (TypeError, ValueError) as e:
         print(e)


print(exp_multi_line("srikanth" , 4))



# Input
#
# a
# 2
# Output
#
# can only concatenate str (not "int") to str
# Here, we try to catch two types of exceptions TypeError and ValueError, which are passed as inside a tuple in the except block.
#
# In the above example, string and an integer cannot be added, so TypeError is caught.
#
# Let's see another example with a different exception.
#
# Input
#
# a
# b
# Output
#
# invalid literal for int() with base 10: 'b'
# In the above example, the second input should have been an integer, but we passed a string 'b'. Therefore, ValueError is raised.
#
# Note: The error which comes first is caught as an exception in case of multiple exceptions.