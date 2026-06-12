Python Project Management CLI Tool
A professional, modular Command-Line Interface (CLI) tool for managing users, projects, and tasks, built with Python. This project follows object-oriented design principles and provides persistent storage using JSON.
Features

    User Management: Add and list users.
    Project Management: Create projects with owners and descriptions.
    Task Management: Add tasks to projects with due dates, assignees, and status tracking.
    Persistent Storage: All data is saved to and loaded from JSON files.
    Professional UI: Uses the tabulate library for clean, grid-based table outputs.
    Input Validation: Validates date formats and ensures data integrity.


Usage
Run the tool using the main.py entry point:
User Management

    Add a user: python3 -m project_management_cli.main user add --id U01 --name "Alice"
    List users: python3 -m project_management_cli.main user list

Project Management

    Add a project: python3 -m project_management_cli.main project add --id P01 --name "Website Redesign" --desc "Revamp the company site" --owner U01
    List projects: python3 -m project_management_cli.main project list

Task Management

    Add a task: python3 -m project_management_cli.main task add --pid P01 --tid T01 --name "Design Mockup" --desc "Create initial UI designs" --due 2024-12-31 --assign U01
    List tasks: python3 -m project_management_cli.main task list --pid P01
