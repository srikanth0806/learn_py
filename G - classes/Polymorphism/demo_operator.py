"""

    Polymorphism in addition(+) operator
       i.integer --> arithmetic operation.
       ii.strings --> concatination. """


# arithmetic operation:
num1 = 1
num2 = 2
print(num1+num2)

#Hence, the above program outputs 3.


# concatination:

str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)

# output: Python Programming

#Here, we can see that a single operator + has been used to carry out
# different operations for distinct data types.
# This is one of the most simple occurrences of polymorphism in Python.




"""

    Polymorphism in Multiplication(*) operator
       i.integer --> multiplication operation.
       ii.strings --> replication """


# Multiplication operation:
num1 = 2 * 4
print(num1)

#Hence, the above program outputs 8.


# replication:

str1 = "Python" * 4

print(str1)

# output: 'PythonPythonPythonPython'

#Here, we can see that a single operator * has been used to carry out
# different operations for distinct data types.
# This is one of the most simple occurrences of polymorphism in Python.