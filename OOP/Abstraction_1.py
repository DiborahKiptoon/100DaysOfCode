#We will use class shapes
#Shape Example
class Shape:

    #constructor
    def __init__(self):
        self.name = ''

    #method: Perimeter
    def area(self):

        #statements
        pass

    #method 2: Area
    def area (self):
        #statements
        pass

    #method 2: Print statement
    def fact (self):
        #statements
        pass
    
         
#Real classes
class circle(Shape):
    def __init__(self):
        self.name = ''
        self.radius = 0

    #method 1
    def CPerimeter(self):
        radius = int(input("Enter the radius: ", ))
        self.radius = radius
        perimeter = 3.142 * (self.radius * 2)
        print(perimeter)

    #method 2
    def CArea(self):
        radius = int(input("Enter the radius: ", ))
        self.radius = radius
        area = 3.142 * self.radius * self.radius
        print(area)


    #method 3
    def Fact (self):
        name = int(input("Enter shape name: ", ))
        self.name = name
        print("The shape is name", self.name)

#Shape 2: Rectangle
class rectangle(Shape):

    #constructor
    def __init__(self):
        self.name = ''
        self.length = 0
        self.width = 0 

    #method 1
    def Rperimeter(self):
        len = int(input("Enter the Length: ", ))
        wid = int(input("Enter the width: ", ))
        self.length = len
        self.width = wid
        perimeter_r = 2*(self.length +self.width)
        print(perimeter_r)

    #method 2
    def RArea(self):
        len = int(input("Enter the Length: ", ))
        wid = int(input("Enter the width: ", ))
        self.length = len
        self.width = wid
        area_r = self.length * self.width
        print(area_r)
    
    #method 3
    def RFact (self):
        name = int(input("Enter shape name: ", ))
        self.name = name
        print("The shape is name", self.name)


#Create objects
rect = rectangle()
circ = circle()





                
