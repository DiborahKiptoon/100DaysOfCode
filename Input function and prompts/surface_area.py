print("Inpu the following")
print("Enter PI measurements")
pi = float(input())
print("Enter the radius")
rad = int(input())
print("Enter the hight")
height= int(input())

#SA of closed cylinder
surf_area = 2*(pi*rad*rad) + 2*pi(rad+rad)*height
print("The surface area is", surf_area)
