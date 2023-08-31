#Question 2:You are the one to prepare your small sibling to go back to school. Given that the shopping budget you have is sh.35000, describe how you will get to decide what to buy for your small sibling as they go back to school in a pseudocode. Finally convert that into python code.


budget = 35000
total_cost = 0
shopping_list = []

print("Budget is sh.35000.")

print("Clothing:")
if budget >= 1000:
    shopping_list.append("School uniforms")
    budget -= 10000
    total_cost += 1

print("School supplies:")
if budget >= 5000:
    shopping_list.append("Notebooks, pens, and pencils")
    budget -= 10000
    total_cost += 1

print("Backpack:")
if budget >= 3000:
    shopping_list.append("Sturdy backpack")
    budget -= 6000
    total_cost += 1

print("Shoes:")
if budget >= 4000:
    shopping_list.append("School shoes")
    budget -= 9000
    total_cost += 1

print("Shopping list:")
for item in shopping_list:
    print(item)

print("Total items purchased:", total_cost)
print("Remaining budget:", budget)
