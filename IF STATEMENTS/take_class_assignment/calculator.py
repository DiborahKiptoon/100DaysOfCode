# Question 2:  Imagine you are working on a calculator to perform all the Mathematical Operations that are involved in a rectangle, rectangular tank, circle, and a cylindrical tank.

import math

print("Welcome to the Math Calculator!")

print("Choose a shape:")
print("1. Rectangle")
print("2. Rectangular Tank")
print("3. Circle")
print("4. Cylindrical Tank")

choice = input("Enter your choice: ")

if choice.isdigit():
    choice = int(choice)
    
    if choice == 1:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        perimeter = 2 * (length + width)
        print("Perimeter of Rectangle:", perimeter)
    elif choice == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        surface_area = 2 * (length * width + width * height + height * length)
        volume = length * width * height
        print("Surface Area of Rectangular Tank:", surface_area)
        print("Volume of Rectangular Tank:", volume)
    elif choice == 3:
        radius = float(input("Enter radius: "))
        circumference = 2 * math.pi * radius
        print("Circumference of Circle:", circumference)
    elif choice == 4:
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        surface_area = 2 * math.pi * radius * (radius + height)
        volume = math.pi * radius ** 2 * height
        print("Surface Area of Cylindrical Tank:", surface_area)
        print("Volume of Cylindrical Tank:", volume)
    else:
        print("Invalid choice. Please select a valid option.")
else:
    print("Invalid input. Please enter a valid numeric choice.")

print("Thank you for using this Calculator!")

