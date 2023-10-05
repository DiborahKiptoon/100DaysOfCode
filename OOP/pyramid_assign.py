#You are tasked with the work of writing a script that will help someone perform the operations to calculate the area, perimeter, volume and surface area of a triangle which becomes a pyramid.
# Write a python script the perform those operations using OOP.

import math

# Triangle Class 
class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

# Pyramid class 
class Pyramid(Triangle):
    def __init__(self, base, height, side1, side2, side3, slant_height):
        super().__init__(base, height, side1, side2, side3)
        self.slant_height = slant_height

    def calculate_volume(self):
        base_area = super().calculate_area()
        return (1/3) * base_area * self.height

    def calculate_surface_area(self):
        base_perimeter = super().calculate_perimeter()
        base_area = super().calculate_area()
        return (0.5 * base_perimeter * self.slant_height) + base_area

# Getting user input for triangle and pyramid parameters
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))
side1 = float(input("Enter the length of side 1 of the triangle: "))
side2 = float(input("Enter the length of side 2 of the triangle: "))
side3 = float(input("Enter the length of side 3 of the triangle: "))
slant_height = float(input("Enter the slant height of the pyramid: "))

# Create object
pyramid = Pyramid(base, height, side1, side2, side3, slant_height)

# Calculate and display results
print(f"Triangle Area: {pyramid.calculate_area()}")
print(f"Triangle Perimeter: {pyramid.calculate_perimeter()}")
print(f"Pyramid Volume: {pyramid.calculate_volume()}")
print(f"Pyramid Surface Area: {pyramid.calculate_surface_area()}")
