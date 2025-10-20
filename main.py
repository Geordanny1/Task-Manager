#!/usr/bin/env python3
import argparse
from utils import *
import sys

parser = argparse.ArgumentParser(description="Manage a list of tasks")
subparsers = parser.add_subparsers(dest="command", required=True)

# --- create ---
create_parser = subparsers.add_parser("create", help="Create a new task")
create_parser.add_argument("--title", required=True, help="Title of the task")
create_parser.add_argument("--description", required=True, help="Description of the task")

# --- update ---
update_parser = subparsers.add_parser("update", help="Update a task")
update_parser.add_argument("--id", required=True, help="ID of the task to update")
update_parser.add_argument("--title", help="New title for the task")
update_parser.add_argument("--description", help="New description for the task")
update_parser.add_argument("--status", choices=["pending", "in-progress", "completed"], help="New status of the task")

# --- delete ---
delete_parser = subparsers.add_parser("delete", help="Delete a task")
delete_parser.add_argument("--id", required=True, help="ID of the task to delete")

# --- list ---
list_parser = subparsers.add_parser("list", help="List all tasks")
list_parser.add_argument("--status", choices=["pending", "in-progress", "completed"], help="Filter by status")

# --- view ---
view_parser = subparsers.add_parser("view", help="View a specific task")
view_parser.add_argument("--id", required=True, help="ID of the task to view")

# --- clear ---
clear_parser = subparsers.add_parser("clear", help="Clear all tasks")
clear_parser.add_argument("--confirm", action="store_true", help="Confirm deletion of all tasks")

args = parser.parse_args()

def main():
    if args.command == "create":
        task = Task(args.title, args.description).get_df()
        save_task(task)
        print("✓ Task created successfully!")
        print(f"ID: {task['ID'].values[0]}")
        print(f"Title: {args.title}")

    elif args.command == "update":
        if not args.title and not args.description and not args.status:
            print("Error: You must specify at least one of --title, --description, or --status to update.")
            sys.exit(1)
        
        result = update_task(args.id, args.title, args.description, args.status)
        if result:
            print(f"✓ Task {args.id} updated successfully!")
        else:
            sys.exit(1)

    elif args.command == "delete":
        result = delete_task(args.id)
        if result:
            print(f"✓ Task {args.id} deleted successfully!")
        else:
            sys.exit(1)

    elif args.command == "list":
        list_tasks(args.status)

    elif args.command == "view":
        view_task(args.id)

    elif args.command == "clear":
        if args.confirm:
            clear_all_tasks()
            print("✓ All tasks cleared successfully!")
        else:
            print("Warning: This will delete all tasks. Use --confirm to proceed.")
            sys.exit(1)

if __name__ == "__main__":
    main()
