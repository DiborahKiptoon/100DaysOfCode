# Initializing variables 
variables = [
    ("Avoid sugary foods", False),
    ("Eat low-calorie foods", False),
    ("Drink more water", False),
    ("Include fruits in your meals", False),
    ("Avoid snacks", False),
]

# for block
for var, default_choice in variables:
    choice = input(f"Do you want to {var}? (yes/no): ").lower()
    if choice == "yes":
        variables[variables.index((var, default_choice))] = (var, True)

# Initializing a list to store daily meal plan
meal_plan = []

# Defining a list of meal options 
meal_options = []

for var, chosen in variables:
    if chosen:
        meal_options.append(var)
    else:
        print(f"You should consider {var.lower()}.")


for day in range(1, 8):
    daily_plan = f"Day {day}: {', '.join(meal_options)}"
    meal_plan.append(daily_plan)


print("\n Eating routine for the week:")
for daily_plan in meal_plan:
    print(daily_plan)
else:
    print("You have successfully planned your eating routine for the week.")
