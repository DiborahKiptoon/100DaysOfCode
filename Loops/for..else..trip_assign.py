#variables = clothes, shoes, beauty_products, camera, passport, visa, money

# List of items to choose from
items = ["clothes", "shoes", "beauty_products", "camera", "passport", "visa", "money"]

# Initializing the variable 
items_packed = []

# for block
for item in items:
    choice = input(f"Do you want to pack {item}? (yes/no): ").lower()
    if choice == "yes":
        items_packed.append(item)
        if len(items_packed) >= 3:
            print("Great job! You've packed at least 3 items for your trip:")
            for packed_item in items_packed:
                print("- " + packed_item)
        else:
            print("You need to pack at least 3 items for your trip. Please pack more essentials.")

