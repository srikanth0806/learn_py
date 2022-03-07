"""
  Python Program to Display Powers of 2
  Using Anonymous Function.
  LOGIC:
       X = 2 ** num
"""


result = list(map(lambda x: 2 ** x , range(0, 10)))
for i in range(0,10):
    print(" 2 power of ", i ,"is", result[i] )
