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

obj=Yourclass()

'''
SOLUTION Q18 : If Yourclass.marks then it will give global value and
If YC.marks then it will give value of object locally not globally!
'''
