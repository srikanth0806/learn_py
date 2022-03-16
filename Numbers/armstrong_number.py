"""
   19.Python Program to Check Armstrong Number.

   NOTE:
      the sum of nth power of each digit is equal to
      the number itself.
      nth power = number of digits in a given number.
      like:
      A positive integer is called an Armstrong number
      of order n if
      abcd... = an + bn + cn + dn + ...
  For example:
    153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
  procedure:
       i.get ecah digit in a number
       ii.to make nth power that number
       iii.add nth power of each number
       iv.finally check out put == given number.
"""
# for i in range
def armstrong_number(num):
    x = str(num)
    l=len(x)
    y = int(x)
    temp = y
    sum=0
    while y > 0:
        r = y % 10
        sum= sum + r **l
        y = y // 10
        print(y, "*********")
    if temp == sum:
        print("the given number is armstrong number.")
    else:
        print("the given number in not armstrong number.")
armstrong_number(153)