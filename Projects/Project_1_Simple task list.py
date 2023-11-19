tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def complete_task(task_index):
    try:
        task_index = int(task_index)
        completed_task = tasks.pop(task_index)
        print(f"Task '{completed_task}' marked as complete.")
    except (ValueError, IndexError):
        print("Error: Invalid task number.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task_index = input("Enter the task number to mark as complete: ")
        complete_task(task_index)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
