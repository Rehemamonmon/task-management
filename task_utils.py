from datetime import datetime

# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Error: Invalid task title.")
        return
    if not validate_task_description(description):
        print("Error: Invalid task description.")
        return
    if not validate_due_date(due_date):
        print("Error: Invalid due date.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]
    if len(pending_tasks) == 0:
        print("No pending tasks.")
    else:
        for i, task in enumerate(pending_tasks):
            print(f"{i + 1}. {task['title']} - Due: {task['due_date']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0
    else:
        completed = len([task for task in tasks if task["completed"]])
        progress = (completed / len(tasks)) * 100
    return progress