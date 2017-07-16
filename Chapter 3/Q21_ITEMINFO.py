'''Q21 Page 65 - Define a class ITEMINFO with following description....'''

class ITEMINFO:
    def __init__(self):
        self.icode=0.0
        self.item_name=''
        self.price=0.0
        self.qty=0.0
        self.discount=0.0
        self.netprice=0.0

    def FindDisc(self):
        if self.qty>=20:
            self.discount=20
        elif self.qty<20 and self.qty>10:
            self.discount=15
        elif self.qty<=10:
            self.discount=0

    def Buy(self):
        self.icode=input("Enter Item Code: ")
        self.item_name=raw_input("Enter name of that Item: ")
        self.price=input("Enter price of that item : ")
        self.qty=input("Enter quantity: ")

    def ShowAll(self):
        print "Intem Code is : ",self.icode
        print "Item name is : ",self.item_name
        print "Price of that item is : ",self.price
        print "Quantity of that item is :",self.qty
        print "Net price is : (price of 1 x quantity) : ",self.price*self.qty
        print "Discount given is : ",self.discount
        print "Final amount to be paid is : ",(self.price*self.qty)-self.discount

obj=ITEMINFO()
obj.Buy()
obj.FindDisc()
obj.ShowAll()
