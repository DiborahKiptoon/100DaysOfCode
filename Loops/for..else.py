#syntax
'''for x in y:
      statement
    else:
         statement
                '''

#Case study 1: Goal is to not be hungry
#The desired conditions
food = [1,2,3] #Food is present
exhausted = 0 # if the level reach 3 of exhaustion they will not cook
guest = 5 # This will be part of else() block

for i in food:
    exhausted = exhausted + 1
    if(exhausted>3):
        print("You can buy food")
    else:
        print("Go to the kitchen and cook")

else:
    if(guest >= 5):
        print("Go buy food")
    else:
        print("Go to the kitchen and cook")                
