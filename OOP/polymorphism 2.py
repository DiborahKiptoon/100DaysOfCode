#Second example of polymorphism
#We will use animal as example

#Origin class
class animal:

    #constructor
    def __init__(self):
        self.movement = ''
        self.sound = ''
        self.name = ''

#Form 1
class Cat(animal):

    #method name
    def getName(self):
        name = input("Enter the Cat name: ", )
        self.name = name
        return self.name

#Form 2 : Dog
class Dog(animal):

    #method name
    def getName_2(self):
        name_2 = input("Enter the dog name: ", )
        self.name = name_2
        return self.name
    

#Form 3
class Parrot(animal):

    #method name
    def getName_3(self):
        name_3 = input("Enter the parrot name: ", )
        self.name = name_3
        return self.name
         
#create object
cat = Cat()
dog = Dog()
parrot = Parrot()


#call method
print(cat.getName())
print(dog.getName_2())
print(parrot.getName_3())





