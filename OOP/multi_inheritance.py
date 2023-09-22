class Supermarket:

    #constructor
    def __init__(self, grocery, detergents, bakery):
        self.grocery = grocery
        self.detergents = detergents
        self.bakery = bakery

    #method : 1
    def getGrocery(self):
        groc = input("Enter your grocery of choice: ", )
        self.grocery = groc
        return self.grocery
    
    #method : 2
    def getBakery(self):
        bake = input("Enter your bakery of choice: ", )
        self.backery = bake
        return self.bakery
    
    #method : 3
    def getDetergents(self):
        deter = input("Enter your detergent of choice: ", )
        self.detergent = deter
        return self.detergent
        


#Base class 2:
class shop:
    def __init__(self, Toiletry, crockery):
        self.toiletry =  crockery
        self.crockery = crockery


#method
def getStuff(self):
    toilet_s = input("Enter yoour toilet essentials: ", )  
    self.toiletry = toilet_s
    return self.toiletry

def getStuff2(self):    
    crock = input("Enter crookery of choice: ", )
    self.crockery = crock
    return self.crockery



#multiple inheritance
#Derived class
class shopping(Supermarket, shop):
    def __init__(self):
        Supermarket.__init__(self, '', '', '')
        shop.__init__(self, '', '')

    #method
    def getList(self):
        print(self.backery)
        print(self.crockery)
        print(self.detergent)
        print(self.toiletry)
        print(self.crockery)

     
# Create objects
shopping = shopping()

#calling the method
print(shopping.getBakery())
print(shopping.getDetergents())
print(shopping.getGrocery())



