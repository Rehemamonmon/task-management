
# Contains all task management functions for the Task Management System

from validation import validate_task_name, validate_task_priority, validate_task_id


def add_task(tasks):
    """
    Prompts the user to enter a task name and priority,
    validates the inputs, and adds a new task dictionary to the tasks list.
    Each task is a dictionary with: id, name, priority, completed.
    """
    print("\n--- Add New Task ---")
    task_name = input("Enter task name: ").strip()

    if not validate_task_name(task_name):
        return

    priority = input("Enter priority (low, medium, high): ").strip().lower()

    if not validate_task_priority(priority):
        return

    # Generate a unique ID based on the current length of the list
    task_id = len(tasks) + 1

    task = {
        "id": task_id,
        "name": task_name,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    print(f"Task '{task_name}' added successfully with ID {task_id}.")


def mark_task_complete(tasks):
    """
    Prompts the user to enter a task ID and marks that task as complete.
    Validates that the task ID exists before marking.
    """
    print("\n--- Mark Task as Complete ---")

    if len(tasks) == 0:
        print("No tasks available to mark as complete.")
        return

    try:
        task_id = int(input("Enter the Task ID to mark as complete: ").strip())
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    if not validate_task_id(task_id, tasks):
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print(f"Task ID {task_id} is already marked as complete.")
            else:
                task["completed"] = True
                print(f"Task '{task['name']}' marked as complete.")
            break


def view_pending_tasks(tasks):
    """
    Displays all tasks that are not yet completed.
    If no pending tasks exist, informs the user.
    """
    print("\n--- Pending Tasks ---")

    pending = [task for task in tasks if not task["completed"]]

    if len(pending) == 0:
        print("No pending tasks. Great job!")
        return

    print(f"{'ID':<5} {'Name':<30} {'Priority':<10}")
    print("-" * 45)
    for task in pending:
        print(f"{task['id']:<5} {task['name']:<30} {task['priority']:<10}")


def track_progress(tasks):
    """
    Displays a summary of total, completed, and pending tasks
    along with a completion percentage.
    """
    print("\n--- Progress Tracker ---")

    total = len(tasks)

    if total == 0:
        print("No tasks found. Add some tasks to track progress.")
        return

    completed = len([task for task in tasks if task["completed"]])
    pending = total - completed
    percentage = (completed / total) * 100

    print(f"Total Tasks   : {total}")
    print(f"Completed     : {completed}")
    print(f"Pending       : {pending}")
    print(f"Progress      : {percentage:.1f}%")