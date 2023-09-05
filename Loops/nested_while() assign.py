#Variables = onions, tomatoes, ginger, garlic, pepper, kales, cabbage, carrots, cucumbers
grocery_inventory = {
    "onions": 10,
    "tomatoes": 15,
    "ginger": 5,
    "garlic": 7,
    "pepper": 12,
    "kales": 20,
    "cabbage": 8,
    "carrots": 10,
    "cucumbers": 6,
}


items_to_restock = []


iteration = 1
restock_needed = True  


while restock_needed:
    print(f"Iteration {iteration}:")
    print("Current Grocery Inventory:")
    
    
    for item, quantity in grocery_inventory.items():
        print(f"{item}: {quantity}")
    
    
    restock_needed = False
    
    
    item_iterator = iter(grocery_inventory.keys())
    try:
        while True:
            item = next(item_iterator)
            quantity = grocery_inventory[item]
            
            if quantity < 10:  
                print(f"Restocking {item}")
                
                grocery_inventory[item] += 10  
                items_to_restock.append(item)
                restock_needed = True  
            
    except StopIteration:
        pass

    if not restock_needed:
        print("No items need restocking. Inventory is up-to-date.")
    
    iteration += 1

print("Final Grocery Inventory:")
for item, quantity in grocery_inventory.items():
    print(f"{item}: {quantity}")

print("Items restocked:", items_to_restock)
