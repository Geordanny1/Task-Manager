import os
import subprocess
import json
import uuid
from datetime import datetime

task = {
    "title": "",
    "description": "no description",
    "date": datetime.today().strftime("%Y-%m-%d"),
    "id": str(uuid.uuid4())
}


def get_title():
    title = input("What do you wanna do?\n")
    task["title"] = title

def get_description():
    user_input = input("Do you want to add a description? (Y/n?)\n")
    if user_input.lower() == "y":
        description = input("please add the description:\n")
        task["description"] = description 

def create_folder():
    if not os.path.exists("tasks"):
        os.mkdir("tasks")
        print("folder create")

def save_task():
    with open(f"tasks/{task['title']}.json", "w") as file:
        json.dump(task, file, indent=4)


    
