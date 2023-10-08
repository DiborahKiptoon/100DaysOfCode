# we will be building a stack using OOP concepts
# In this method, I'll be building a stack using Linked Lists
#code starts here.

class Info:

    def __init__(self, value):
        self.value = value
        self.next = None  #this is to add data to the list

#creating a stack
class Stack:

    #initialization
    def __init__(self):
        self.head = Info("head")
        self.size = 0

    #intialization to take in string values
    def __str__(self):
        new= self.head.next
        out = " "

        #Loop to take in the value
        while new:
            out += str(new.value) + "->"
            new = new.next

            return out[ :+2]
        
    #get the size
    def getSize(self):
        return self.size
    
    #checking if our stack is empty
    def isEmpty(self):
        return self.size == 0
    
    #to check the topmost data item in the stack
    def Top(self):

        #to avoid errors, I will raise an exception
        if self.isEmpty():
            raise Exception("Your stack is Empty")
        return self.head.next.value
    
    #Push method:- Adds data items to the stack
    def push(self, value):
        base = Info(value)           #to add data item to the stack
        base.next = self.head.next    # to proceed to the next data item

        self.head.next = base
        self.size += 1

    #Pop Method: Delets data items from the stack
    def pop(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


# Create the stack object
if __name__ == "__main__":
    stack1 = Stack()

    #loop to create the range of the information I want stored in the stack
    for w in range(1, 12):
        stack1.push(w)
        print(stack1)

    #Loop to initialize the range of which I want to delete info from my stack
    for _ in range(2, 8):
        remove = stack1.pop()
        print("Popped info: ", remove)
    print(stack1)

