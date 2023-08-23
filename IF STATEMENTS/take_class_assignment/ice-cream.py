#Question 3 : Imagine you went to an ice-cream inn and you bought an ice cone with 2 scoops of ice cream. Consider the shape of your cone and calculate the following 

import math

pi = 22/7
cone_radius = float(input("Enter cone radius: "))
scoop_radius_1 = float(input("Enter scoop radius 1: "))
scoop_radius_2 = float(input("Enter scoop radius 2: "))

cone_height = math.sqrt(cone_radius ** 2 - (scoop_radius_1 - scoop_radius_2) ** 2)

cone_surface_area = pi * cone_radius * (cone_radius + math.sqrt(cone_radius ** 2 + cone_height ** 2))

cone_volume = (1/3) * pi * cone_radius ** 2 * cone_height

scoop_1_volume = (4/3) * pi * scoop_radius_1 ** 3

scoop_2_volume = (4/3) * pi * scoop_radius_2 ** 3

total_volume = cone_volume + scoop_1_volume + scoop_2_volume

print("Cone Surface Area:", cone_surface_area)
print("Cone Volume:", cone_volume)
print("Scoop 1 Volume:", scoop_1_volume)
print("Scoop 2 Volume:", scoop_2_volume)
print("Total Volume:", total_volume)

