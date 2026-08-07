"""
Challenge : Terminal-Based Task List Manager

Create a python script that lets users manage a to-do list directly from
the terminal.

Your program should :
1. Allow users to :
   - Add a task
   - View all tasks
   - Mark a task as completed 
   - Delete a task 
   - Exit the app
2. Save all tasks in a text file named 'tasks.txt' so data persists
between runs.
3. Display tasks with an index number and a ✅ if completed.

Example :
1. Add task
2. View task 
3. MArk task as completed 
4. Delete task
5. Exit

Example Output :
Your task :

Buy groceries || not_done
Finish Python project || done
Read a book || not_done

Bonus :
- prevent empty tasks from being added
- Validate task numbers before completing/deleting 
"""

import os 
TASK_FILE = 'tasks.txt'

def load_task():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding="utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text" : text, "done" : status == "done"})

    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, 'w', encoding="utf-8") as f:
        for task in tasks:
            status  = "done" if task["done"] else "Not done"
            f.write(f"{task['text']} || {status}\n")

def display_tasks(tasks):
    if not tasks:
        print(f"No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            checkbox = "✅" if task["done"] else " "
            print(f"{i}, [{checkbox}] {task['text']}")

    print()

def task_manager():
    tasks = load_task()

    while True:
        print("\n ------Task List Manager------.")
        print("1. Add Task.")
        print("2. View Tasks.")
        print("3. Mark Task as completed.")
        print("4. Delete Task.")
        print("5. Exit.")

        Choice = input("Choose an option (1-5) : ").strip()

        match Choice:
            case "1":
                text = input("Enter your task : ").strip()
                if text:
                    tasks.append({"text" : text, "done" : False})
                    save_tasks(tasks)
                else:
                    print("Task connot be empty.")

            case "2":
                display_tasks(tasks)

            case "3":
                display_tasks(tasks)
                try:
                    number = int(input("Enter task number "))
                    if 1 <= number <= len(tasks):
                        tasks [number-1]["done"] = True
                        save_tasks(tasks)
                        print("Task marked as DONE")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a number.")

            case "4":
                display_tasks(tasks)
                try:
                    number = int(input("Enter task number to delete. "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number-1)
                        save_tasks(tasks)
                        print(f"Task removed : {removed ['text']}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a number.")

            case "5":
                print("Exiting Task Manager.")
                break
            case _:
                print("Please Choose a valid option.")

task_manager()
                



