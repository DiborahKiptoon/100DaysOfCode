class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: KSh.{self.salary:.2f}")

# Create instances (objects) of the Employee class
employee1 = Employee(7001, "Diborah Kiptoon", "Manager", 60000)
employee2 = Employee(6784, "KJ Debbie", "Developer", 50000)

# Display employee details
print("Employee 1 Details:")
employee1.display_details()

print("\nEmployee 2 Details:")
employee2.display_details()