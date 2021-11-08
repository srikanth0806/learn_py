#Python Program for compound interest.
     #Formula to calculate compound interest annually is given by:
        #C
        #Compound Interest = A – P
             #Where,
          #a is amount
          #P is principle amount
          #R is the rate and
          #T is the time span
def compound_interest(p, r, t):
    a = p * (pow((1 + r / 100), t))
    compoundinterest = a - p
    return compoundinterest


print("compound_interest is : ",
      compound_interest(10000, 8, 2))
