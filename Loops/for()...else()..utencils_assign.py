#variables

#children: The number of children expected at the event.
#adults: The number of adults expected at the event.
#number_of_guests.
#type_of_food = "finger foods," "buffet," "barbecue"
#type_of_drinks = "soft drinks," "juices," "alcoholic beverages").
#Plates
#Forks
#knives
#glasses

# Input variables
children = int(input("Enter the number of children: "))
adults = int(input("Enter the number of adults: "))
type_of_food = input("Enter the type of food you plan to serve: ")
type_of_drinks = input("Enter the type of drinks you plan to serve: ")

# Calculate the total number of guests
number_of_guests = children + adults

# Initialize variables to store utensil quantities
plates = 0
forks = 0
knives = 0
glasses = 0

# For block (Calculating utensil quantities based on the type of food and drinks0
for guest in range(number_of_guests):
    if type_of_food == "finger foods":
        plates += 1
        forks += 1
    elif type_of_food == "buffet":
        plates += 1
        forks += 1
        knives +=1
    elif type_of_food == "barbecue":
        plates += 1
        forks += 1
        knives +=1
    if type_of_drinks == "soft drinks":
        glasses += 1
    elif type_of_drinks == "juices":
        glasses += 1
    elif type_of_drinks == "alcoholic beverages":
        glasses += 1

# Output the quantities of utensils needed
print(f"You need {plates} plates, {forks} forks, and {glasses} glasses for your event.")
