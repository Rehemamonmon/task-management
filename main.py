
# Entry point for the Task Management System

from task_utils import add_task, mark_task_complete, view_pending_tasks, track_progress


def display_menu():
    """Displays the main menu options to the user."""
    print("\n=============================")
    print("   Task Management System   ")
    print("=============================")
    print("1. Add Task")
    print("2. Mark Task as Complete")
    print("3. View Pending Tasks")
    print("4. Track Progress")
    print("5. Exit")
    print("=============================")


def main():
    """
    Main function that runs the Task Management System.
    Maintains the tasks list and routes user input to the correct function.
    """
    tasks = []  # List of task dictionaries

    print("Welcome to the Task Management System!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_task_complete(tasks)
        elif choice == "3":
            view_pending_tasks(tasks)
        elif choice == "4":
            track_progress(tasks)
        elif choice == "5":
            print("Thank you for using the Task Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()