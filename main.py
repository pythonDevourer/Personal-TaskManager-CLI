# main.py
from managers.taskmanager import TaskManager
from models.task import Task
from datetime import datetime

tm = TaskManager()

print("Welcome to Personal TaskManager CLI")
print("Feel free to visit the repo! https://github.com/pythonDevourer/Personal-TaskManager-CLI")

operation_text = """
What operation do you want to do?
    r: read all tasks
    c: create new task
    q: quit
"""

while True:
    operation = input(operation_text).strip().lower()

    if operation == "r":
        tasks = tm.get_all()
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for t in tasks:
                status = "✅" if t.status else "❌"
                print(f"{t.id}: {t.name} | {status}")
        print()

    elif operation == "c":
        name = input("Enter task name: ")
        task = Task(name=name)
        tm.create(task)
        print(f"Task '{task.name}' created!\n")

    elif operation == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid operation. Please try again.\n")
