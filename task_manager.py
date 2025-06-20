import os
import json
import sys
import uuid
from datetime import datetime
from typing import Dict, Tuple, List, Optional
from tabulate import tabulate

# Configuración de directorios
TASKS_DIR = "tasks"
TASKS_FILE = os.path.join(TASKS_DIR, "tasks.json")
LAST_ID_FILE = os.path.join(TASKS_DIR, "last_id.json")

# Crear directorio si no existe
os.makedirs(TASKS_DIR, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")


def safe_input(prompt: str) -> str:
    try:
        user_input = input(prompt)
        if user_input.strip().lower() == "q":
            print("\nGoodbye! Thank you for using Task Manager.")
            sys.exit(0)
        return user_input
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting gracefully...")
        sys.exit(1)


def safe_int_input(prompt: str) -> int:
    while True:
        user_input = safe_input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print(f"Error: '{user_input}' is not a valid integer. Please try again.")


class Task:
    def __init__(
        self,
        title: str = "no title",
        info: str = "empty",
        completed: bool = False,
        date: str = today,
        task_id: Optional[int] = None,
    ) -> None:
        self.title = title
        self.date = date
        self.info = info
        self.completed = completed
        self.task_id = task_id or self.generate_id()

    @staticmethod
    def generate_id() -> int:
        """Genera un ID único autoincremental"""
        try:
            if not os.path.exists(LAST_ID_FILE):
                with open(LAST_ID_FILE, "w") as f:
                    json.dump({"last_id": 0}, f)

            with open(LAST_ID_FILE, "r") as f:
                data = json.load(f)

            new_id = data["last_id"] + 1
            data["last_id"] = new_id

            with open(LAST_ID_FILE, "w") as f:
                json.dump(data, f)

            return new_id
        except Exception as e:
            print(f"Error generating ID: {e}")
            return int(uuid.uuid4().int & (1 << 31) - 1)  # Fallback UUID

    def get_data(self) -> Dict:
        return {
            "id": self.task_id,
            "title": self.title,
            "date": self.date,
            "info": self.info,
            "completed": self.completed,
        }

    def __str__(self) -> str:
        return f"Task [ID: {self.task_id}]: {self.title}"

    def __repr__(self) -> str:
        return f"Task(id={self.task_id}, title={self.title}, info={self.info}, completed={self.completed}, date={self.date})"


# Funciones de persistencia
def load_tasks() -> List[Dict]:
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks: List[Dict]) -> None:
    try:
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f, indent=2)
    except Exception as e:
        print(f"Error saving tasks: {e}")


def update_task_in_list(tasks: List[Dict], old_task: Dict, new_task: Dict) -> None:
    index = next((i for i, t in enumerate(tasks) if t["id"] == old_task["id"]), -1)
    if index != -1:
        tasks[index] = new_task


def update_status(task_dict: Dict) -> None:
    task_dict["completed"] = not task_dict["completed"]
    task_dict["date"] = today


def select_task(task_list: List[Dict]) -> Tuple[Dict[int, Dict], int]:
    if not task_list:
        print("No tasks available to select.")
        return {}, -1

    options = {}
    print("\nAvailable Tasks:")
    print("-" * 40)

    for index, task in enumerate(task_list):
        options[index] = task
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['title']} (ID: {task['id']})")

    print("-" * 40)

    while True:
        try:
            user_selection = safe_int_input("\nSelect a task (or 'q' to quit): ")
            if user_selection in options:
                return options, user_selection
            else:
                valid_indices = ", ".join(map(str, options.keys()))
                print(
                    f"Error: {user_selection} is not a valid option. Please select from: {valid_indices}"
                )
        except ValueError:
            continue


def show_tasks_no_info(tasks: List[Dict]) -> None:
    if not tasks:
        print("\nNo tasks available.")
        return

    headers = ["ID", "Title", "Status", "Last Updated"]
    table_data = []
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        table_data.append([task["id"], task["title"], status, task["date"]])

    print(tabulate(table_data, headers=headers, tablefmt="rounded_grid"))


def show_info_task(tasks: List[Dict]) -> None:
    if not tasks:
        print("\nNo tasks available.")
        return

    headers = ["ID", "Title", "Description"]
    table_data = []
    for task in tasks:
        table_data.append([task["id"], task["title"], task["info"]])

    print(tabulate(table_data, headers=headers, tablefmt="rounded_grid"))

