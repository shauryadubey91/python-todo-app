# To-Do List Application using Python 

def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("\nNo tasks found.\n")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("\nNo tasks found.\n")


def add_task():
    task = input("Enter new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!\n")


def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted successfully!\n")
        else:
            print("Invalid task number!\n")
    except:
        print("Invalid input!\n")


while True:
    print("==== TO-DO LIST ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")
