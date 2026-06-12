
import json
from datetime import datetime

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["user_id"], data["name"])

class Project:
    def __init__(self, project_id, name, description, owner_id):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.owner_id = owner_id  # User ID of the project owner
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "owner_id": self.owner_id,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(data["project_id"], data["name"], data["description"], data["owner_id"])
        project.tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
        return project

class Task:
    def __init__(self, task_id, name, description, due_date, assigned_to_id, status="Pending"):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.due_date = due_date  # Stored as string 'YYYY-MM-DD'
        self.assigned_to_id = assigned_to_id # User ID of the assignee
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "due_date": self.due_date,
            "assigned_to_id": self.assigned_to_id,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["task_id"],
            data["name"],
            data["description"],
            data["due_date"],
            data["assigned_to_id"],
            data["status"]
        )
