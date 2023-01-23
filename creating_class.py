# instance or object of a class--> same meaning

class Item:
    pay_rate = 0.8 #class attributes applies to all the instances #after 20% discount
    def __init__(self, name: str, price: float, quantity):  #constructor : an example of a magic method # you can assign defaault values. eg. quantity = 0
        #Run validtions to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 1) #creating an instance of a class #attributes of the instance passed as arguments 
item1.apply_discount()
print(item1.price)

# print(Item.__dict__) #All attributes for class level
# print(item1.__dict__) # All attributes for instance level
# print(item2.calculate_total_price())

