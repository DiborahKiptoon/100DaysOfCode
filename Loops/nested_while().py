#Nested while() loop
# in this loop, we will be exploring how to write nested while() loops code
# syntax
'''while(condition):
    while(condition):
        while(comdition):
            statements
    statements
statements'''

#Case study 1 Turning on a particular appliance in the house
#socket_var, Electricity_var, presence_var, Time, mood_var

#variables
socket = 0  #0 rep off and 1 rep on
electricity = 0
presence = 0
Time = 0   # Goal of time = 3
mood = "Happy"  #if Block
#process
presence = presence + 1
electricity = electricity + 1
socket = socket + 1

#Nested while() starts here
while(presence == 1):
    while(electricity == 1):
        while(socket == 1):
            Time = Time + 3
            if(mood == "Happy" and Time <= 3):
                print("You can watch television or Listen to Music for: ", Time)
            else:
                print("Relax and go to sleep")
                break
        
        else:
            if(socket != 1):
                print("Turn on the Socket")
            else:
                print("You can use your phone to stream")
        break
        
    else:
            print("Relax for KPLC To do their thing")
    break
       
else:
    if(presence != 1):
        print("Get home first")
    
        
