#Case study 3: Fruits
class Fruits:

    #Constructor
    def __init__(self, shape, color, sugar_level, price):
        self.shape = shape
        self.color = color
        self.sugar_level = sugar_level
        self.price = price

    #method 1: shape
    def getShape(self):
        return self.shape

    #method 2: color
    def getColor(self):
        return self.color

    #method 3: Calculate sugar_level
    def getShape(self):
        self.sugar_level = 0
        new_level = self.sugar_level + (234/40)
        return new_level

    #method 4: price
    def getPrice(self):
        self.price = 0
        no_of_pieces = self.price + 14
        cost = 15
        total_price = no_of_pieces * cost
        return total_price
    

    #create object
    Fruits = []
    fruit = Fruits("Cresent", "yellow", 0, 0)
    fruit_2 = Fruits ("Circle", "Orange", 0,0)
    fruit_3 = Fruits("Oval", "Black", 0, 0)
    fruit_4 = Fruits ("Oval", "green", 0, 0)
    fruit_5 = Fruits ("Oval", "yellow", 0, 0)
    fruit_6 = Fruits ("Oval", "Cylindrical", 0, 0)


    #calling our object
    print(fruit_4.getSugar())
    print(fruit_6.getPrice())
    print(fruit_3.getShape())
    print(fruit_5.getColor())

      


#