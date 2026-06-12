import json
import os
from .models import User, Project, Task

class DataManager:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        self.users_file = os.path.join(data_dir, "users.json")
        self.projects_file = os.path.join(data_dir, "projects.json")

    def _load_json(self, filepath):
        if not os.path.exists(filepath) or os.stat(filepath).st_size == 0:
            return []
        with open(filepath, "r") as f:
            return json.load(f)

    def _save_json(self, filepath, data):
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

    def load_users(self):
        users_data = self._load_json(self.users_file)
        return [User.from_dict(data) for data in users_data]

    def save_users(self, users):
        users_data = [user.to_dict() for user in users]
        self._save_json(self.users_file, users_data)

    def load_projects(self):
        projects_data = self._load_json(self.projects_file)
        return [Project.from_dict(data) for data in projects_data]

    def save_projects(self, projects):
        projects_data = [project.to_dict() for project in projects]
        self._save_json(self.projects_file, projects_data)
