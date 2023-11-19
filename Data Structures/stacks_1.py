#A stack is built using two particular methods one being using lists and the other one using arrays.
#In order to access data inside a stack one must use a method called pop()
#A simple demo
mystack = []

#We will add data using the append function(This is how we push data inside a stack)
mystack.append("Harry")
mystack.append("Mary")
mystack.append("Mercy")
mystack.append("Melvin")
print(mystack)

#How to access data inside a stack
#We are going to use the pop() method to access the data items
print(mystack.pop())
print(mystack)

newstack = []

newstack.append(20.1)
newstack.append(40)
newstack.append(70.98)
newstack.append(67.77)
newstack.append(11.87)
newstack.append(30)

#Demostrating other functions associated with stack
#Empty() method