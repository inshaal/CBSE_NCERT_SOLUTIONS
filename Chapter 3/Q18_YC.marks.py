''' Q18 Yourclass question on page 63'''

class Yourclass:
    marks=10 #class variable
    name="ABC"

    def __init__(Self,marks,name):
        self.marks=marks #instance attribute
        self.name=name

    def dislay(self):
        print marks
        print name

YC=Yourclass(5,"name") #any arguement
"""
If command is YC.display()
the output will be:

10
"ABC"

Which means that it will give output as class variables.

If 'print self.marks' and 'print self.name' is in the display(self),
then the output will be:

5
"name"

"""
