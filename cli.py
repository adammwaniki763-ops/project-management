import argparse
import sys
from .data_manager import DataManager
from .models import User, Project, Task
from .utils import validate_date, format_header

def tabulate(table_data, headers=None, tablefmt="grid"):
    rows = []
    if headers:
        rows.append(headers)
    rows.extend(table_data)
    return "\n".join(" | ".join(str(item) for item in row) for row in rows)


def main():
    parser = argparse.ArgumentParser(description="Python Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # User commands
    user_parser = subparsers.add_parser("user", help="Manage users")
    user_subparsers = user_parser.add_subparsers(dest="user_command")
    
    add_user = user_subparsers.add_parser("add", help="Add a new user")
    add_user.add_argument("--id", required=True, help="Unique user ID")
    add_user.add_argument("--name", required=True, help="User name")

    list_users = user_subparsers.add_parser("list", help="List all users")

    # Project commands
    project_parser = subparsers.add_parser("project", help="Manage projects")
    project_subparsers = project_parser.add_subparsers(dest="project_command")
    
    add_project = project_subparsers.add_parser("add", help="Add a new project")
    add_project.add_argument("--id", required=True, help="Unique project ID")
    add_project.add_argument("--name", required=True, help="Project name")
    add_project.add_argument("--desc", required=True, help="Project description")
    add_project.add_argument("--owner", required=True, help="User ID of the owner")

    list_projects = project_subparsers.add_parser("list", help="List all projects")

    # Task commands
    task_parser = subparsers.add_parser("task", help="Manage tasks")
    task_subparsers = task_parser.add_subparsers(dest="task_command")
    
    add_task = task_subparsers.add_parser("add", help="Add a task to a project")
    add_task.add_argument("--pid", required=True, help="Project ID")
    add_task.add_argument("--tid", required=True, help="Unique task ID")
    add_task.add_argument("--name", required=True, help="Task name")
    add_task.add_argument("--desc", required=True, help="Task description")
    add_task.add_argument("--due", required=True, help="Due date (YYYY-MM-DD)")
    add_task.add_argument("--assign", required=True, help="User ID of the assignee")

    list_tasks = task_subparsers.add_parser("list", help="List tasks for a project")
    list_tasks.add_argument("--pid", required=True, help="Project ID")

    args = parser.parse_args()
    
    manager = DataManager()
    
    if args.command == "user":
        users = manager.load_users()
        if args.user_command == "add":
            print(format_header("Adding New User"))
            if any(u.user_id == args.id for u in users):
                print(f"Error: User ID '{args.id}' already exists.")
                return
            new_user = User(args.id, args.name)
            users.append(new_user)
            manager.save_users(users)
            print(f"User '{args.name}' added successfully.")
        elif args.user_command == "list":
            print(format_header("User List"))
            if not users:
                print("No users found.")
            else:
                table_data = [[u.user_id, u.name] for u in users]
                print(tabulate(table_data, headers=["ID", "Name"], tablefmt="grid"))

    elif args.command == "project":
        projects = manager.load_projects()
        users = manager.load_users()
        if args.project_command == "add":
            print(format_header("Adding New Project"))
            if any(p.project_id == args.id for p in projects):
                print(f"Error: Project ID '{args.id}' already exists.")
                return
            if not any(u.user_id == args.owner for u in users):
                print(f"Error: Owner ID '{args.owner}' does not exist.")
                return
            new_project = Project(args.id, args.name, args.desc, args.owner)
            projects.append(new_project)
            manager.save_projects(projects)
            print(f"Project '{args.name}' added successfully.")
        elif args.project_command == "list":
            print(format_header("Project List"))
            if not projects:
                print("No projects found.")
            else:
                table_data = [[p.project_id, p.name, p.owner_id] for p in projects]
                print(tabulate(table_data, headers=["ID", "Name", "Owner"], tablefmt="grid"))

    elif args.command == "task":
        projects = manager.load_projects()
        users = manager.load_users()
        project = next((p for p in projects if p.project_id == args.pid), None)
        
        if not project:
            print(f"Error: Project ID '{args.pid}' not found.")
            return

        if args.task_command == "add":
            print(format_header(f"Adding Task to {project.name}"))
            if not validate_date(args.due):
                print(f"Error: Invalid date format '{args.due}'. Use YYYY-MM-DD.")
                return
            if any(t.task_id == args.tid for t in project.tasks):
                print(f"Error: Task ID '{args.tid}' already exists in this project.")
                return
            if not any(u.user_id == args.assign for u in users):
                print(f"Error: Assignee ID '{args.assign}' does not exist.")
                return
            new_task = Task(args.tid, args.name, args.desc, args.due, args.assign)
            project.add_task(new_task)
            manager.save_projects(projects)
            print(f"Task '{args.name}' added to project '{project.name}'.")
        elif args.task_command == "list":
            print(format_header(f"Task List: {project.name}"))
            if not project.tasks:
                print(f"No tasks found for project '{project.name}'.")
            else:
                table_data = [[t.task_id, t.name, t.due_date, t.status] for t in project.tasks]
                print(tabulate(table_data, headers=["ID", "Name", "Due Date", "Status"], tablefmt="grid"))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
