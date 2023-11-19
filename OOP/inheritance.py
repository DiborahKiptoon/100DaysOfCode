#Derive class
class Electric_shop:

    #constructor
    def __init__(self, pd_name, quantity, price):
        self.name = pd_name
        self.quantity = quantity
        self.price = price

#Derived class 1
class name(Electric_shop):
     
     #create constructor
     def __init__(self, pd_name, quantity, price):
         self.name = pd_name
         self.quantity = quantity
         self.price = price


    #method
     def getname(self):
         name = input("Enter the device name: ",)
         self.name = name
         return self.name        


#Inherit from name
class Laptop(name):
    def getPrice(self):
        price = int(input("Enter the price: ", ))
        self.sprice = price
        return self.sprice

 #create object

lappy = Laptop ("Asus", 0, 0)


print(lappy.getPrice())
print(lappy.getName())

   
    
       