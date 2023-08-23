
#Question 1: Imagine you are about to create a budget for what you will be spending for the month of September.

total_income = float(input("Enter your total income: $"))

# Get expense details from the user
expense_name_1 = input("Enter expense name 1: ")
expense_amount_1 = float(input("Enter expense amount 1: $"))

expense_name_2 = input("Enter expense name 2: ")
expense_amount_2 = float(input("Enter expense amount 2: $"))

expense_name_3 = input("Enter expense name 3: ")
expense_amount_3 = float(input("Enter expense amount 3: $"))

# Calculate total expenses
total_expenses = expense_amount_1 + expense_amount_2 + expense_amount_3

# Calculate savings
savings = total_income - total_expenses

# Display budget summary
print("\nBudget Summary for September:")
print("Total Income: $" + str(total_income))
print("Total Expenses: $" + str(total_expenses))
print("Savings: $" + str(savings))

