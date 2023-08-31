# Question 2:5You are about to purchase a ticket for something or some chilling over the weekend. You have to decide whether you will attend the movies or you’ll go for sport. Write a pseudocode that will take you through the steps of deciding what you will do and how much you will spend. Then convert that into a python code.


budget = float(input("What is your budget for the weekend? "))

if budget < 0:
    print("Invalid budget entered. Please enter a valid budget.")
else:
    print("Great! Now let's decide your activity:")
    activity_choice = input("Press 'M' for Movies or 'S' for Sports: ")

    if activity_choice.upper() == 'M':
        movie_ticket_price = 200
        if budget >= movie_ticket_price:
            print("You can go to the movies!")
            remaining_budget = budget - movie_ticket_price
            print("You will have $" + str(remaining_budget) + " left after purchasing the ticket.")
        else:
            print("Your budget is not enough for a movie.")
    
    elif activity_choice.upper() == 'S':
        sports_event_ticket_price = 700
        if budget >= sports_event_ticket_price:
            print("You can go to the sports event!")
            remaining_budget = budget - sports_event_ticket_price
            print("You will have $" + str(remaining_budget) + " left after purchasing the ticket.")
        else:
            print("Your budget is not enough for a sports event.")
    
    else:
        print("Invalid choice entered. Please choose either 'M' for Movies or 'S' for Sports.")
