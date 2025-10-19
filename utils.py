from datetime import datetime
from task import Task

import pandas as pd

import os
import time

import random
import string

def get_title():
    title = input("What do you wanna do?\n")
    return title

def get_description():
    user_input = input("Do you want to add a description? (Y/n?)\n")
    if user_input.lower() == "y":
        description = input("please add the description:\n")
        return description
    else:
        return "-no description provide-"

def generate_custom_id():
    timestamp = str(int(time.time()))
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"ID-{timestamp}-{random_chars}"


def create_file():
    if not os.path.exists("task.txt"):
        with open("task.txt", "w") as task:
            new_table = create_table()
            task.write(new_table.get_string())


def save_file(data_frame) -> None:
    data_frame.to_pickle("task_list.pkl")


def get_task_list():
    return pd.read_pickle("task_list.pkl")

