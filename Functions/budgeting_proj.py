#Budget tracker

#expenses
#income
#goals

#logic
#unemployed.....30,30,30,10
#employed .....50, 30, 20
#zero based


#output
#decision
#goal

#first list of variables will be income variables

salary = int(input('Enter your income: '))
sidehustle=int(input('Enter your income: '))

#Expenses
utilityBills=int(input('Enter your utility expense: '))
grocery = int(input('Enter your grocery expense: '))
allowances = int(input('Enter your allowances: '))

#Goals
goal1='Improve my setup'
goal2='Go on vacation'
goal3='Start a business'
goal4 = 'Education bills'

mygoal = goal1

#if elif be used for logic
if(mygoal == goal1):
    newincome=salary +sidehustle
    if(newincome >=40000):
        expense_net = newincome * 50/100
        allowances_net = newincome *30/100
        savings_net=newincome * 20/100 
        print(expense_net)
        print(allowances_net)
        print(savings_net)

    elif(newincome >= 50000):
        expense_net = newincome * 30/100
        allowances_net = newincome *30/100
        savings_net=newincome * 30/100
        leisure_net = newincome * 10/100
        print(expense_net)
        print(allowances_net)
        print(savings_net)
        print(leisure_net)

    else:
        print("Sorry, your income category isn't listed")

elif(mygoal == goal2):
                


