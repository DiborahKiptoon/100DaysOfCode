#Question 3: You are about to do some cleaning in your house. You have a lot to do. Write a pseudocode that will represent how you will perform your cleaning from the first chore to the last. Then convert it into a python code.

print("Start with washing dishes")

laundry_choice = input("Do you have laundry to do? (yes/no) ")
if laundry_choice.lower() == "yes":
    print("Move on to doing laundry")
   
else:
    print("No laundry today.")

print("Time to organize items")


wipe_choice = input("Do you want to wipe windows and surfaces? (yes/no) ")
if wipe_choice.lower() == "yes":
    print("Wipe windows and surfaces")
   
else:
    print("Skipping window and surface wiping.")

print("Vacuum and mop the floors")


print("Dust and clean furniture")


print("Clean the bathroom")


trash_choice = input("Do you need to take out the trash? (yes/no) ")
if trash_choice.lower() == "yes":
    print("Take out the trash")
 
else:
    print("Trash is already taken out.")

print("All cleaning tasks are complete!")
