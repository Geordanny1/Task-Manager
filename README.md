# Task Manager CLI

A simple command-line task manager to help you keep track of your to-dos. Built with Python and pandas.

## What it does

Basically, it lets you create tasks, update them, delete them, and see what you've got on your plate. Nothing fancy, just a straightforward way to manage your tasks from the terminal.

## Installation

Make sure you have Python 3 installed. Then install the dependencies:

```bash
pip install -r requirements.txt
```

That's it! You're ready to start managing tasks.

## How to use it

### Creating a task

```bash
python3 main.py create --title "Buy groceries" --description "Need milk, eggs, and bread"
```

This creates a new task with a unique ID. You'll see the ID printed out - save it if you need to update or delete the task later.

### Listing all your tasks

```bash
python3 main.py list
```

Shows all your tasks in a nice table. You can also filter by status:

```bash
python3 main.py list --status pending
python3 main.py list --status completed
```

### Viewing a specific task

```bash
python3 main.py view --id ID-1729123456-ABC123
```

Shows all the details for that task. If you get the ID wrong, don't worry - it'll show you all available tasks so you can copy the right one.

### Updating a task

You can update the title, description, or status:

```bash
python3 main.py update --id ID-1729123456-ABC123 --status completed
python3 main.py update --id ID-1729123456-ABC123 --description "Updated description"
python3 main.py update --id ID-1729123456-ABC123 --title "New title" --status in-progress
```

Status options are: `pending`, `in-progress`, `completed`

### Deleting a task

```bash
python3 main.py delete --id ID-1729123456-ABC123
```

If you mess up the ID, the program will show you all your tasks so you can grab the correct ID.

### Clearing everything

```bash
python3 main.py clear --confirm
```

This deletes ALL tasks. The `--confirm` flag is there to make sure you don't accidentally nuke everything.

## Files structure

- `main.py` - The main program that handles all the commands
- `utils.py` - Helper functions for saving, loading, and managing tasks
- `task.py` - The Task class definition
- `task_list.pkl` - Where your tasks get saved (created automatically)
