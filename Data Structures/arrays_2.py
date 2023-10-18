#They hold only one data type in a single array of data items
# The data items are enclosed in curly brackets
# An array is mutable( data items stored in the diff indices can be changed, as long as its of the same data type)

#syntax
#import the array module
#array_name = stated_array.array the module("data_type", [data items])

#we will have a demo with the methods

#demo starts here
#imports
import array as Type

#create the array
my_array = Type.array("i", [23, 14, 17, 34])
my_sec_array = Type.array("i")

#methods
#Append()
'''var = 23
var_2 = 45
var_3 = int(input("Enter a numeral value: "))
var_4 = int(input("Enter a numeral value: "))

my_sec_array.append(var)
my_sec_array.append(var_2)
my_sec_array.append(var_3)
my_sec_array.append(var_4)
'''
# Insert()
array_mine = Type.array("c")

#variables
var_a = "x"
var_b = "t"

array_mine.insert()


#printing
#print(my_array)
print(my_array[ :2])
print(my_sec_array)