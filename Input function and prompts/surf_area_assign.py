#Write a python program that will prompt the user to perform the calculations of Area, surface area and volume of a cuboid
print("Kindly enter the Dimensions")
print("Length")
length = int(input())

print("Width")
width = int(input())

print("Height")
height = int(input())

surface_area = 2 * ((length * width) + (width * height) + (length * height))
print("Surface Area is", surface_area)

volume = length * width * height
print("Volume is", volume)

