"""FUNCTION OVERLOADING IS NOT POSSIBLE IN PYTHON""" 
"""However, if it was possible, the following code would work."""
def area(a): #Area of circle
    from math import pi
    sol=pi*(r**2)
    print sol, "is area of circle"

def area(a,b): #Area of rectangle
    sol= a*b
    print sol, "is area of rectangle"

def area(a,b,c): #Area of triangle
    s= (a+b+c)/2.0
    sol= (s(s-a)(s-b)(s-c))^0.5
    print sol, "is area of triangle"

a= raw_input("Enter a: ")
b= raw_input("Enter b: ")
c= raw_input("Enter c: ")

#Error will come if only a and b are given because python takes the latest definiton of function. so only area of triangle can be calculated.

'''Below- REQUIRED BECAUSE YOU NEED TO CHECK IF THE FUNCTION HAS GIVEN TWO ARGUEMENTS OR THREE
-as it's done in C++, Java or other languages that support function overloading'''
ta= bool(a)
tb= bool(b)
tc= bool(c)

if ta:
    a= float(a)
    if not (tb and tc):
        area(a)
    elif tb and (not tc):
        b= float(b)
        area(a,b)
    elif (tb and tc):
        b= float(b)
        c= float(c)
        area(a,b,c)
"""Though, you can directly use area(a) and area(a,b) [but a and b should be float!] and mention that it will output error that it takes 3 arguements.
Because the third defitinition of function area(a,b,c) overwrites the previous definitions"""

"""It's possible using module/s: https://pypi.python.org/pypi/overload"""
