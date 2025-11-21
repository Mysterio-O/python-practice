def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Quit")


def add_task(tasks):
    title = input("Enter the task: ")
    task = {"title": title, "completed": False}
    tasks.append(task)
    print(f'Task "{title}" added!')


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f'{index}. [{status}] {task["title"]}')


def mark_task_as_done(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as done: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task["title"]}" deleted!')
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    tasks = []  # This will be our list of tasks

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_as_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
