total_saved = 0
fridge_cost = 50000
microwave_cost = 7000
airfryer_cost = 15000

while total_saved < (fridge_cost + microwave_cost + airfryer_cost):
    print("Current savings:", total_saved)
    additional_savings = float(input("Enter the amount you're saving now: "))
    total_saved += additional_savings

    if total_saved >= fridge_cost:
        print("Congratulations! You can buy a fridge.")
        total_saved -= fridge_cost
    elif total_saved >= microwave_cost:
        print("Congratulations! You can buy a microwave.")
        total_saved -= microwave_cost
    elif total_saved >= airfryer_cost:
        print("Congratulations! You can buy an airfryer.")
        total_saved -= airfryer_cost
    else:
        print("Keep saving to buy the electronics.")

else:
    print("You have saved enough to buy all the electronics!")
    print("Remaining savings:", total_saved)

    while total_saved < (fridge_cost + microwave_cost + airfryer_cost):
        print("\nContinue saving for the remaining electronics.")
        additional_savings = float(input("Enter the amount you're saving now: "))
        total_saved += additional_savings

print("Congratulations! You've purchased all the electronics!")
