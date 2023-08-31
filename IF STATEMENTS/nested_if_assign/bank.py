#Question 1:You are supposed to run an errand in the bank. Write a pseudocode that will represent your wholesome decision to go to the bank, run the errand of your choice and perform the mini-activities you want to perform in the bank. Afterwards convert that into python code
 
print("Let's go to the bank!")
documents = ["ID", "business registration"]

print("While at the bank, let's take care of a few things:")
personal_balance = 750.00  
print(f"Checking personal account balance: ${personal_balance}")

if personal_balance < 1000.00:
    withdrawal_amount = 500.00
    print(f"Withdrawing ${withdrawal_amount} from ATM")
else:
    print("Personal account balance is sufficient.")

print("Inquiring about business account options")

print("Now, let's open a new business account!")
provided_documents = ["ID", "business registration"]
print(f"Provided documents: {provided_documents}")

account_type = "savings"  
if account_type == "savings":
    print("Selected account type: Savings")
    account_number = "1234567890"
    initial_deposit = 500.00
    print(f"Received account number: {account_number}")
    print(f"Initial deposit required: ${initial_deposit}")
else:
    print("Selected account type: Checking")
    account_number = "9876543210"
    initial_deposit = 300.00
    print(f"Received account number: {account_number}")
    print(f"Initial deposit required: ${initial_deposit}")
