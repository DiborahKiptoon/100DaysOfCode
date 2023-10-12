
# this is a sequential data structure
#it follows a systematic way of data storage
# Its mutable(changable)

#List data stucture demos
# We will have 2 examples and then perform some operations on them

#Creating list
Fruits = []

#Inserting operations
#hard-code var
FA = "Banana"
FB = "Apple"
FC = "Mango"
FD = "Orange"

#Prompting the user
#input() the variables
'''FE = input("Enter the fruit Name: ", )
Fruits.append(FE)
FG = int(input("Enter a random Number: ", ))
Fruits.append(FG)'''

#append() to add the data items
Fruits.append(FB)
Fruits.append(FA)
Fruits.append(FC)
Fruits.append(FD)

#The append() function is used to insert items/add data items to a list
#data type
#print(Fruits)

#insert() function
var = "Pineapple"
var_1 = 65
var_3 = True

#adding data item using the insert function
Fruits.insert(4, var)
Fruits.insert(0, var_1)
Fruits.insert(2, var_3)

#The insert() function adds data items into a list using a format of [index_value, variable(data item)]


'''print(Fruits)
print(Fruits[3])
print(Fruits[2])'''

#Concatinate
# Concatination is the process of combining two lists to make one whole new list
Fruit = ["Oranges", " Avocado", " Grapes"]

#concatinate symbol is +
new_fruits = Fruit + Fruits

print(new_fruits)
