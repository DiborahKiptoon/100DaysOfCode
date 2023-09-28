#The existence of an object in many forms
# we will have 2 examples
#The examples will be of shapes

#Case study 1: Circle
class circle:

    

    #constructor
    def __init__(self):
        self.pi = 3.142
        self.radius = 0


    #method: get radius
    def Radius(self):
        radius = int(input("Kindly enter the radius: ", ))
        self.radius = radius
        print("The radius is: ", self.radius)


    #form 1: Cylinder pi r2h
class cylinder(circle):
       
        #method
        def render(self):
            height = int(input("Kindly enter the height: ", ))
            vol = self.pi * self.radius * self.radius * height
            print("The volume is: ", vol)

    #Form 2: sphere(circle)
class sphere(circle):
     
     #method
     def SArea(self):
          surface = 4/3 * self.radius * self.radius * self.radius * self.pi
          print("The surface area is: ", surface)


#create objects
sphere1 = sphere()
cylinder1 = cylinder()


#methods
print(sphere1.Radius())
print(sphere.SArea())





  
    
