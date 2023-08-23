#Question 5: 5. In your current living situation, kindly assess what you need to make a decision on and pick one situation and create a flow diagram of your process of decision making and convert it into python code.

#For the December holiday, if I have more than 14 days off, I’ll go to vacation. If I have less than 14 days off and more than 5 days, I will visit friends and family. If I have less than 5 days, I I’ll rest at my house"

days_off = int(input("How many days off do you have for the December holiday? "))

if days_off > 14:
    print("You should go on vacation.")
elif days_off > 5 and days_off <= 14:
    print("Consider visiting friends and family.")
else:
    print("It's a good time to stay at home and relax.")

