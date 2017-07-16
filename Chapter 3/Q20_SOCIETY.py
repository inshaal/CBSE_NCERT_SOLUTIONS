''' Create the class SOCIETY with the following information...'''

class SOCIETY:
    def __init__(self):
        self.soc_name=''
        self.house_no=0.0
        self.members=0.0
        self.flat=''
        self.income=0.0

    def allocate_flat(self):
        if self.income>=25000:
            self.flat='A'
        elif self.income<25000 and self.income>=20000:
            self.flat='B'
        elif self.income<15000:
            self.flat='C'

    def Inputdata(self):
        self.soc_name=raw_input("Enter society name :")
        self.house_no=input("Enter house number :")
        self.members=input("Enter no. of members : ")
        self.income=input("Enter income :")

    def Showdata(self):
        print "Society Name is : ",self.soc_name
        print "House no. us : ",self.house_no
        print "Number of members are : ",self.members
        print "Flat type is : ",self.flat
        print "Income is : ",self.income
obj=SOCIETY()
obj.Inputdata()
obj.allocate_flat()
obj.Showdata()
