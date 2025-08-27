from models import Task
from utils.context_managers import JsonContextManager

class TaskManager:
    def __init__(self):
        self.json_path = "data/tasks.json"
        self.tasks: list[Task] = []
        self.load_tasks()

    def load_tasks(self):
        with JsonContextManager(self.json_path, "r") as file:
            self.tasks = [Task.model_validate(item) for item in file.data]

    def save_tasks(self):
        with JsonContextManager(self.json_path, "w") as file:
            for task in self.tasks:
                file.add(task.model_dump())

    def create(self, task_data: Task):
        if Task.model_validate(task_data):
            self.tasks.append(task_data)
            self.save_tasks()
        return task_data

    def get_all(self):
        return self.tasks