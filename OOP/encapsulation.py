#Encapsulation ....data hiding
#We will be defining public and private members in code
#private = single underscore(_) or double underscore(__)


#First example(pricing case study)
class price:

    #Constructor
    def __init__(self):
        self._price1 = 400

    #method 1
    def sellPrice(self):
        sellPrice = self._price1 * (120/100)
        print("The selling price is: ", sellPrice)

    #method 2
    '''def getProfit(self):
        profit = sellPrice - self.price1
        print("The profit is: ", profit)'''
    

#Create object
MarkedP = price()

#Call the method
print(MarkedP.sellPrice())

    #Example 2
class Person:
        

        #constructor
        def __init__ (self):
            self.__name = ""
            self.__salary = 0
            self._status = ""


        #create method
        def getName(self):
            name = input("Enter your name: ", )
            self._name = name
            print("Emplyee Name: ", self._name)


        #method 2 : salary
        def getSalry(self):
            sal = int(input("Enter the salary amount: ", ))
            self.__salary = sal
            print("Salary due: ", self._salary)


        #method 3: emp status
        def Status(self):
            stat = input("Enter Emp status")
            self._status = stat
            print("Employment Status: ", self._status)

        #
class NewSalary(Person):
            


            #method: Calculate new salary
            def newSalary(self):
                sal_new = self._salary *(115/100)
                print("New Salary: ", sal_new)


#call objrct
Alice = Person()
Alice = NewSalary()

 #Call on Methods
print(Alice.getSalary())
print(Alice.newSalary())        






            


       

    
