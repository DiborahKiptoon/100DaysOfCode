#As a backend developer, you noticed that the API your team developed is not storing the correct data hence not performing the best operations in the ecommerce communication section.
#Create a python script that will use OOP Concepts to use the right methods for any communication from the users of the app.

#class
class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def send_message(self, message):
        # Simulate sending a message
        print(f"Message sent to {self.username}: {message}")

#AdminUser class (inheriting from User)
class AdminUser(User):
    #constructor
    def __init__(self, user_id, username, email, admin_level):
        # Call the constructor of the parent class (User)
        super().__init__(user_id, username, email)
        self.admin_level = admin_level

    def send_message_to_all(self, message, users):
        # Simulate sending a message to all users
        print(f"Admin message from {self.username} (Level {self.admin_level}): {message}")
        for user in users:
            user.send_message(message)

# Create object
user1 = User(1, "Diborah", "diborah@gmail.com")
user2 = User(2, "debbie", "debbie2@yahoo.com")
admin1 = AdminUser(101, "Admin1", "admin1@ecom.com", 2)

#user and admin interactions
user1.send_message("Hi, I'm interested in buying baby products")
user2.send_message("Sure, what would you like to know about the baby products?")
admin1.send_message_to_all("Important announcement: New products added!", [user1, user2])
