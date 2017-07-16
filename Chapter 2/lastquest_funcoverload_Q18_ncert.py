"""FUNCTION OVERLOADING IS NOT POSSIBLE IN PYTHON"""
"""However, if it was possible, the following code would work."""
def volume(a): #For volume of cube
    vol=a**3
    print vol, "is volume of cube"
def volume(a,b,c): #volume of cuboid |b-height
    vol=a*b*c
    print vol, "is volume of cuboid" 
def volume(a,b): #volume of cylinder |a-radius|b-height
    from math import pi
    vol= pi*(a**2)*b
    print vol, "is volume of cylinder"
a=raw_input("Enter dimension1: ")
b=raw_input("Enter dimension2: ")
c=raw_input("Enter dimension3: ")
#note that these are raw inputs and a the defined function will not work for strings
#We're using raw_input so that we can check the truth value the variables that are supposed to be strings in the code below
'''
Notice Python takes the latest definition of that function. So if all three values are provided for a,b & c Python will give an error
stating it takes only 2 arguments but 3 given.
'''

'''Below- REQUIRED BECAUSE YOU NEED TO CHECK IF THE FUNCTION HAS GIVEN TWO ARGUEMENTS OR THREE
-as it's done in C++, Java or other languages that support function overloading'''
#bool, because if the value is not a string, then the function will be execeuted without that corresponding variable
ta=bool(a)
tb=bool(b)
tc=bool(c)
if ta:
    a=float(a)
    if not (tb and tc):
        volume(a)
    elif tb and (not tc):
        b=float(b)
        volume(a,b)
    elif (tb and tc):
        b=float(b)
        c=float(c)
        volume(a,b,c)

"""
If the raw_input statements weren't mentioned in the above code. Then it can be simply represented as volume(a,b) or volume(a)
and mentioned that this will give out error that the function takes 3 arguements as the function is overwritten by the third definition
"""

"""It's possible using module/s: https://pypi.python.org/pypi/overload"""
