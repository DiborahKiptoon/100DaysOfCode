#function method
def DecimalToBinary(n):
    return("{0:b}".format(int(n)))

#call function
#Write codes to convert the following into Bits
#12
a = DecimalToBinary(12)
print(a)

#34
b = DecimalToBinary(34)
print(b)

#65
c = DecimalToBinary(65)
print(c)

#456
d = DecimalToBinary(456)
print(d)

#Write a python program using user defined Functions that will allow you to convert the following into Bits and To decimals
def Binary_To_Decimal(b):
    decimal_number = int(b, 2)
    return decimal_number


#110111
x = Binary_To_Decimal("110111")
print(x)
#010111100
y = Binary_To_Decimal("010111100")
print(y)
#1001000110
z = Binary_To_Decimal("1001000110")
print(z)