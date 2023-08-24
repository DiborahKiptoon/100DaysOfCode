#Question 3: You are the chair of an event committee set to have an event on the 29th day of August. Describe to us in a pseudocode how you will get to decide the flow of events or activities in that particular event. Then convert that into python code.

events_list = ["Morning Prayer", "Worship Service", "Community Lunch", "Workshops", "Music Concert"]

print("Welcome to the Church Event on August 29th!")
print("Here's the schedule for the day:")

event_index = 1
total_events = len(events_list)

if event_index < total_events:
    event = events_list[event_index]
    print("Time for", event)
    
    if event == "Morning Prayer":
        print("Gather for a peaceful morning prayer session.")
    else:
        event_index += 1
        if event == "Worship Service":
            print("Join us in the main hall for a worship service.")
        else:
            event_index += 1
            if event == "Community Lunch":
                print("Enjoy a delicious community lunch in the courtyard.")
            else:
                event_index += 1
                if event == "Workshops":
                    print("Participate in various workshops and activities.")
                else:
                    event_index += 1
                    if event == "Music Concert":
                        print("Experience a soulful music concert in the evening.")
                    else:
                        print("Stay tuned for more surprises!")

print("Thank you for joining us in this wonderful event!")
