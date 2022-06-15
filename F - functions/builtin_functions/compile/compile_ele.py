"""
write a python programme to perform the compile() function.

Python compile() Function

defiition:
    Python compile() function takes source code as input and
    returns a code object which is ready to be executed and
    which can later be executed by the exec() function.

Syntax:
    compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)


Parameters:

Source – It can be a normal string, a byte string, or an AST object
Filename -This is the file from which the code was read.
If it wasn’t read from a file, you can give a name yourself.
Mode – Mode can be exec, eval or single.
a. eval – If the source is a single expression.
b. exec – It can take a block of a code that has Python statements,
class and functions and so on.
c. single – It is used if consists of a single interactive statement
Flags (optional) and dont_inherit (optional) – Default value=0.
It takes care that which future statements affect the compilation of the source.
Optimize (optional) – It tells optimization level of compiler. Default value -1.
Python compile() function example
Example 1: Simple compile() example in Python.
Here filename is mulstring and exec mode allows the use of
exec() method and the compile method converts the string to Python code object.


# Python code to demonstrate working of compile().

# Creating sample sourcecode to multiply two variables
# x and y.
srcCode = 'x = 10\ny = 20\nmul = x * y\nprint("mul =", mul)'

# Converting above source code to an executable
execCode = compile(srcCode, 'mulstring', 'exec')

# Running the executable code.
exec(execCode) """


"""
Output:

mul = 200"""

#Example 2:  Another demonstration working of compile

# Another Python code to demonstrate working of compile()."""
x = 50

# Note eval is used for single statement
a = compile('x', 'test', 'single')
print(type(a))
exec(a)

"""
Output:

<class 'code'>
50 """

"""
Example 3: Python compile function from file
In this example, we will take main.py file with some string display methods,
 and then we read the file content and compile it to code the object 
 and execute it.

main.py:"""


String = "Welcome to Geeksforgeeks"
print(String)
Code: """Here we will read the file content as a string and
then compile it to a code object.

# reading code from a file
f = open('main.py', 'r')
temp = f.read()
f.close()
 
code = compile(temp, 'main.py', 'exec')
exec(code)


# Output:
# 
# Welcome to Geeksforgeeks 

# Example 4: Compile() with eval()
Here eval is used when the source is a single expression.


# Another Python code to demonstrate
# working of compile() with eval.
x = 50
 
# Note eval is used for statement
a = compile('x == 50', '', 'eval')
print(eval(a))


Output:

True 


# # Applications: 
# # If the Python code is in string form or is an AST object, and 
# you want to change it to a code object, then you can use compile() method.
# # The code object returned by the compile() method can later be 
# called using methods like: exec() and eval() which will execute dynamically 
# generated Python code.



