import pandas as pd
from datetime import datetime
import time
import string
import random

def get_custom_id():
    """Generate a unique ID for each task"""
    timestamp = str(int(time.time()))
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"ID-{timestamp}-{random_chars}"

class Task:
    def __init__(self, title, description, id=None, date=None, status="pending"):
        self.title = title
        self.description = description
        self.date = date if date else datetime.today().strftime("%Y-%m-%d")
        self.status = status
        self.id = id if id else get_custom_id()
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_id(self):
        return self.id
    
    def get_date(self):
        return self.date
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        """Update the status of the task"""
        self.status = status
    
    def mark_completed(self):
        """Mark the task as completed"""
        self.status = "completed"
    
    def mark_in_progress(self):
        """Mark the task as in progress"""
        self.status = "in-progress"
    
    def get_df(self):
        """Convert task to a pandas DataFrame"""
        return pd.DataFrame({
            "TITLE": [self.get_title()],
            "DESCRIPTION": [self.get_description()], 
            "DATE": [self.get_date()], 
            "STATUS": [self.get_status()], 
            "ID": [self.get_id()]
        })
    
    def __str__(self):
        return f"[TITLE]\n{self.title}\n[DESCRIPTION]\n{self.description}\n[DATE]\n{self.date}\n[STATUS]\n{self.status}\n[ID]\n{self.id}"
    
    def __repr__(self):
        return f"Task(title='{self.title}', status='{self.status}', id='{self.id}')"
