#Question 4: Imagine you are working in a company that requires an increase in salary to be determined by the arrival of the employees at exactly 9.30am consecutively from Monday to Friday otherwise there is no increase. The increase in salary is 55% of the basic salary. 

arrival_time = input("Enter arrival time9: ")
day_of_week = input("Enter day of the week: ")
basic_salary = float(input("Enter your basic salary: "))

if day_of_week.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    if arrival_time == '9:30am':
        raise_amount = 0.55 * basic_salary
        print("Congratulations! You get a raise of", raise_amount)
    else:
        print("No raise for arriving late.")
else:
    print("Weekends are not considered for raises.")
