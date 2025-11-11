#  Problem Statement:  
# Create a command-line To-Do List app that lets users add, view, and delete tasks during a session.

#  What You'll Learn:  
# - List operations in Python  
# - Using loops and conditionals  
# - Handling user input  
# - Basic CLI app logic

#  Python Code:

todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"Tasks are here:")
            print(f"{i}. {task}")

def add_task(task):
    todo_list.append(task)
    print("Task added.")

def delete_task(index):
    if 0 < index <= len(todo_list):
        removed = todo_list.pop(index - 1)
        print(f"Deleted: {removed}")
    else:
        print("Invalid task number.")
while True:
    print("\n=== To-Do List ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        try:
            idx = int(input("Enter task number to delete: "))
            delete_task(idx)
        except ValueError:
                 print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")


#  Sample Interaction:  

# Choose an option (1-4): 2  
# Enter task: Learn Python  
# Task added.

# Choose an option (1-4): 1  
# 1. Learn Python

#  Output:  
# Tasks listed and managed via CLI
