
from ..models import User, Project, Task

def test_user_creation():
    user = User("U001", "Alice")
    assert user.user_id == "U001"
    assert user.name == "Alice"

def test_project_creation():
    project = Project("P001", "Project A", "Description A", "U001")
    assert project.project_id == "P001"
    assert project.name == "Project A"
    assert project.owner_id == "U001"
    assert len(project.tasks) == 0

def test_task_addition():
    project = Project("P001", "Project A", "Description A", "U001")
    task = Task("T001", "Task 1", "Desc 1", "2024-12-31", "U001")
    project.add_task(task)
    assert len(project.tasks) == 1
    assert project.tasks[0].task_id == "T001"

def test_model_serialization():
    user = User("U001", "Alice")
    user_dict = user.to_dict()
    new_user = User.from_dict(user_dict)
    assert new_user.user_id == user.user_id
    assert new_user.name == user.name
