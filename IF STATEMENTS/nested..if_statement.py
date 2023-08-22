#Case university selection
#Student side decision
distance = 1    #1 = near, 0 = fear
cluster = 40
convinience = 1
upkeep = 1    # 1 = expensive, 0 = affordable
cost = 1    #1 = affordable, 0 = expensive

#Nested If structure
if(cluster >= 35):
    if(convinience == 1):
        if(upkeep < 1):
            if(cost == 1):
                print("Select the University")
            else:
                print("Look for another school")
        else:
            print("Look for affordable school")
    else:
        print("Decide on wether to study only or work only")                

else:
    if(convinience == 1):
        if(upkeep == 0):
            print("You can do the course")
        else:
            print("choose another course")
    else:
        print("Choose another university")            
    


