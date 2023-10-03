#Arrays hold only one data type
# We are practising the use of arrays in data structures 
# We've learned that arrays store data that is of one data type
#Syntax
'''
import array as r
array_name = stated_arr.array the module("data_type", [data items])'''

#Code starts here
import array as Type

#create my array
'''my_array = Type.array('i', [23, 14, 18, 10])
my_sec_array = Type.array('i')

#Printing
print(my_array)

print(my_array[0:2])

#methods
#Append()
var = 23
var_2 = 45
var_3 = int(input("Enter numerical value: "))
var_4 = int(input("Enter numerical value: "))

my_sec_array.append(var)
my_sec_array.append(var_2)
my_sec_array.append(var_3)
my_sec_array.append(var_4)

print(my_sec_array)'''

#insert()
import array as r
new_array = r.array("k")
var_a = "h"
var_b = "q"
var_c = input("Enter new character valu: ")
var_d = input("Enter new character valu: ")

new_array.insert(1,var_a)
print(new_array)
