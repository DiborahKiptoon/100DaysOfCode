#Question 1: Imagine you are about to prepare dinner, you have only a budget of sh. 1500, write a pseudocode that will help you decide on what to buy to fit your budget after deciding what you will have for super. Then convert it to python code

print("Welcome to the Dinner Budget Planner!")

super_choice = input("What would you like to have for supper? (githeri_viazi/ugali_nyama/rice_beans): ")
budget = 1500

if super_choice == "githeri_viazi":
    githeri_viazi_price = 200
    remaining_budget = budget - githeri_viazi_price
    if remaining_budget >= 0:
        print("You can buy githeri with viazi for dinner.")
    else:
        print("Your budget is too low for githeri with viazi.")
elif super_choice == "ugali_nyama":
    ugali_nyama_price = 450
    remaining_budget = budget - ugali_nyama_price
    if remaining_budget >= 0:
        print("You can buy ugali with nyama for dinner.")
    else:
        print("Your budget is too low for ugali with nyama.")
elif super_choice == "rice_beans":
    rice_beans_price = 350
    remaining_budget = budget - rice_beans_price
    if remaining_budget >= 0:
        print("You can buy rice and beans for dinner.")
    else:
        print("Your budget is too low for rice and beans.")
else:
    print("Invalid choice. Please select a valid option.")




