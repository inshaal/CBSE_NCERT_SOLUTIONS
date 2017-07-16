''' Q17 Yourclass question on page 63'''

class Yourclass:
    marks=10 #class variable
    name="ABC"
    
    def __init__(Self,marks,name):
        self.marks=marks #instance attribute
        self.name=name

    def dislay(self):
        print marks
        print name

obj=Yourclass() #THIS IS THE MISSING STATEMENT.
