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


#Example 2
work=5
vacation=2
day = 0

#for block()
for i in range(work):
    day = day + 1
    if(day<=work):
        print("wake up early in the morning")
    else:
        print("You can sleep in")    
else:
    day=day+6
    if(day>work):
        print("You can wake up late!")
    else:
        print("You can wake up early")


#example 3
my_list = [1,23,34,15,17,18,37,45,21,2]
patt = "x"

#for()Block starts
for i in my_list:
    if(i<45):
        patt = patt * 9
        print(patt)
    elif(i<37):
        patt = patt * 8
        print(patt)
    elif(i<34):
        patt = patt * 7
        print(patt)
    elif(i<23):
        patt = patt * 6
        print(patt)
    elif(i<21):
        patt = patt * 5
        print(patt)
    elif(i<18):
        patt = patt * 4
        print(patt)
    elif(i<17):
        patt = patt * 3
        print(patt)
    elif(i<15):
        patt = patt * 2
        print(patt)
    elif(i<1):
        patt = patt * 5
        print(patt)
else:
    print(my_list)                               
        
        
               