#Case study 2 Company protocal
#Ecommerce company
class Complaint:

    #constructor
    def __init__(self):
        self.name = ''
        self.sku_no = 0
        self.complaint = ''

    #method 1: get complain
    def complaint(self):
        #statements
        pass

    #method 3: get info
    def info(self):
        #statements
        pass


    #method 3: submit
    def submit(self):
        #statements
        pass

#client 1
class Client_1(Complaint):

    #constructor
    def __init__(self):
        self.name = ''
        self.complaint = ''
        self.sku_no = ''

    #method 1
    def comp1(self):
        complaint = input("Enter the client concerns: ", )
        self.complaint = complaint
        print("The client's issue is: ", self.complaint) 


    #method 2
    def info1(self):
        Nclient = input("Enter the client name: ", )
        sku_no = int(input("Enter sku number: ", ))
        self.sku_no = sku_no
        self.name = Nclient
        print("Client name is: ", self.name)
        print("SKU Number is: ", self.sku_no)


    #method 3
    def status(self):
        status = input("Is the issue resolved?: ", ).lower

        #Decision tree
        if(status == 'yes'):
            print("The compliant has been resolved successfully!")
        else:
            print("The complaint needs attention")

#Create object
Mark = Client_1()


#print methods

print(Mark.comp1())
print(Mark.info1())
print(Mark.status())




