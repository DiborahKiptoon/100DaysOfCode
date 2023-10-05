
# Define the User class
class User:
    def __init__(self, user_id, username, email, house_preferences):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.house_preferences = house_preferences
    def set_house_preferences(self, house_preferences):
        self.house_preferences = house_preferences

    def display_user_info(self):
        print(f"User ID: {self.user_id}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Preferences: {self.house_preferences}")

# Create instances (users) of the User class
user1 = User(1, "Diborah", "diborah@gmail.com", {})

# Ask the user for input
user_city = input("Enter your preferred city: ")
user_location = input("Enter your preferred location: ")
user_budget = float(input("Enter your budget: Ksh. "))

# Set user preferences based on input
user1.set_house_preferences({"City": user_city, "location": user_location, "budget": user_budget})

# Display user information
print("\nUser 1 Information:")
user1.display_user_info()