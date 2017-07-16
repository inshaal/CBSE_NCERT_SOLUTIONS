''' Q17 Yourclass question on page 63'''

class Yourclass:
    marks=10 #class variable
    name="ABC"
    
    def __init__(self,marks,name):
        self.marks=marks #instance attribute
        self.name=name

    def dislay(self):
        print marks
        print name

obj=Yourclass(10,"ABC") #THIS IS THE MISSING STATEMENT.
#or
obj=Yourclass
