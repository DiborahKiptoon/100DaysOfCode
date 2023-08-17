#Shopping scenario. Write a code that will help you to decide the budget of the things you want to go shopping for and determine how many items you get to buy with that budget.

# Input: Number of items you want to buy
items = int(input("Enter the number of items you want to buy: "))

# Define the budgets based on the number of items
budget_1 = 500  # $500 budget for items < 50
budget_2 = 1000  # $1000 budget for items >= 50

# Calculate the budget based on the number of items
if items < 50:
    budget = budget_1
    max_items_affordable = items
else:
    budget = budget_2
    max_items_affordable = budget_2 // cost_per_item  # Assuming each item costs the same

# Calculate how many items can be bought with the budget
cost_per_item = budget / max_items_affordable
items_affordable = budget // cost_per_item

print("Your budget is $" + str(budget))
print("You can afford to buy", items_affordable, "items.")


#Career scenario. Write a code that will help you decide on what will influence your career choice.
# Analyze the inputs and provide career choice suggestions
print("Welcome to the Career Choice Assistant!")

# Gather user input on various factors
passion = input("Are you passionate about your work? (yes/no): ")
skills = input("Do you possess the necessary skills for a specific career? (yes/no): ")
salary = input("Is salary an important factor for you? (yes/no): ")
growth = input("Do you value career growth opportunities? (yes/no): ")
work_life_balance = input("Is work-life balance important to you? (yes/no): ")

# Analyze the inputs and provide career choice suggestions
if passion == "yes":
    if skills == "yes":
        print("You should consider pursuing a career that aligns with your passion and skills.")
    else:
        print("You might want to work on developing the necessary skills for a career you're passionate about.")
else:
    if salary == "yes":
        print("A career with higher earning potential might be a good fit for you.")
        if growth == "yes":
            print("Look for careers that offer both high salary and growth opportunities.")
    else:
        if growth == "yes":
            print("Prioritize careers that offer significant opportunities for career advancement.")
            if work_life_balance == "yes":
                print("Seek careers that balance growth opportunities with a good work-life balance.")
        else:
            print("Consider exploring a wide range of careers to find the best fit for your values and goals.")


#Gifting Scenario. Write a code that will help you find the best gift to give someone who has done something that impressed you or made you want to gift them.
print("Welcome to the Gift Selection Assistant!")

impressed_action = input("What did do that impressed you? ")

if "helped" in impressed_action.lower():
    print("A thoughtful thank-you card and a bouquet of flowers could be a great gesture.")
else:
    if "achieved" in impressed_action.lower():
        print("Consider giving them a book related to their interest or a small personalized gift.")
    else:
        if "created" in impressed_action.lower():
            print("A creative DIY kit or a set of art supplies might be a fantastic gift choice.")
        else:
            if "organized" in impressed_action.lower():
                print("A planner or an organizational tool could be a useful and appreciated gift.")
            else:
                print("Think about their interests and hobbies to choose a gift that suits them best.")
