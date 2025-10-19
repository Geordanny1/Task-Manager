from datetime import datetime
from prettytable import PrettyTable
from task import Task

import re
from io import StringIO

import os
import time

import random
import string


def create_task():

    create_file()

    table = PrettyTable()
    table.field_names = ["TITLE", "DESCRIPTION", "DATE", "STATUS", "ID"]

    date = datetime.today().strftime('%Y-%m-%d')
    custom_id = generate_custom_id()
    title = get_title()
    description = get_description()

    new_task = Task(title, description, date, custom_id)

    table.add_row(new_task.get_table())







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

def create_table():

    return table


def create_file():
    if not os.path.exists("task.txt"):
        with open("task.txt", "w") as task:
            new_table = create_table()
            task.write(new_table.get_string())




create_task()
