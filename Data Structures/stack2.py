#This a demonstration of how to create a stack from a module
#The module being used is called deque
#The module also holds the methods used to get information about a stcak

#imports
from collections import deque
my_stack = deque()

#Append()
my_stack.append(8)
my_stack.append(10)
my_stack.append(4)
my_stack.append(7)
my_stack.append(8)
my_stack.append(6)
my_stack.append(67)


print(my_stack.Size())



