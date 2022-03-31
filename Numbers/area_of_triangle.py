""" Python Program to Calculate the Area of a Triangle.

      # FORMULA : 1/2 * B *H
       HERE,
           B=BASE
           H=HIGHT """

def area_of_triangle():
    b=float(input("enter the height of the triangle:"))
    h=float(input("enter the base of triangle:"))
    return 1/2 * b * h
print("area of the triangle:",area_of_triangle())

