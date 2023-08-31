
#variables
pat=10

#nested for() Incremental pattern
'''for i in range(0, pat):
    for j in range (0, i+1):
        print("*", end="")
    print() '''   

#nested for() decremental pattern
for i in range(pat, 0, -1):
    for j in range(0, i):
        print("*", end="")
    print()

#Brushing teeth
#tooth

#variables
week=7
toothpaste =1
toothbrush =1
baking_soda = 5 #for()
mirror = 1
water = 7 #for()

#Nested for()
for i in range(0, week):
    for j in range (water):
        for w in range (baking_soda):
            if(toothpaste == 1):
                if(toothbrush == 1):
                    print("You can brrush your teeth!")
                else:
                    print("Go buy new toothbrush")
            else:
                print("Go buy tootpase")
        else:
            if(toothpaste == 1 and toothbrush == 1):
                print("Go and Brush your teeth")        






