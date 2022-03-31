# Python Program to Solve Quadratic Equation.

# SOLUTION:
""" The standard form of a quadratic equation is:

                 ax2 + bx + c = 0, where
                 a, b and c are real numbers and
                 a ≠ 0
The solutions of this quadratic equation is given by:

                (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a) """


def quardratic_equation():
    a=int(input("enter the value of a:"))
    b = int(input("enter the value of b:"))
    c = int(input("enter the value of c:"))
    return (-b+(b**2-4*a*c)** 0.5) / (2*a),(-b-(b**2-4*a*c)** 0.5) / (2*a)

print("the solution of qruardratic equation is:" ,quardratic_equation())

