#Convert the question 1 into Python Code while writing the Pseudocode that will outline the steps you will have to take to complete it.
class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.completed = False

    def complete_task(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, deadline):
        task = Task(name, deadline)
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            status = "Done" if task.completed else "Pending"
            print(f"{task.name} (Deadline: {task.deadline}) - Status: {status}")

    
# Create a To-Do List
my_todo_list = ToDoList()

# Add tasks
my_todo_list.add_task("Go shopping", "Tomorrow")
my_todo_list.add_task("Go to gym", "Today")
my_todo_list.add_task("Code", "Next week")

# Complete a task
my_todo_list.tasks[1].complete_task()

# Show tasks
my_todo_list.show_tasks()
