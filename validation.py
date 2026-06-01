
# Handles all input validation for the Task Management System


def validate_task_name(task_name):
    """
    Validates that a task name is not empty.
    Returns True if valid, False otherwise.
    """
    if len(task_name) == 0:
        print("Error: Task name cannot be empty.")
        return False
    return True


def validate_task_priority(priority):
    """
    Validates that the priority is one of: low, medium, high.
    Returns True if valid, False otherwise.
    """
    valid_priorities = ["low", "medium", "high"]
    if priority.lower() not in valid_priorities:
        print(f"Error: Priority must be one of {valid_priorities}.")
        return False
    return True


def validate_task_id(task_id, tasks):
    """
    Validates that a task ID exists in the task list.
    Returns True if valid, False otherwise.
    """
    if len(tasks) == 0:
        print("Error: No tasks available.")
        return False

    ids = [task["id"] for task in tasks]
    if task_id not in ids:
        print(f"Error: Task ID '{task_id}' not found.")
        return False
    return True