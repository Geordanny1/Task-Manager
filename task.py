class Task:
    def __init__(self, title, description, date, id, status = "Not Completed"):
        self.title = title
        self.description = description
        self.date = date
        self.status = status
        self.id = id

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
    
    def completed(self):
        self.status = "COMPLETED"

    def get_table(self):
        return [self.get_title(), self.get_description(), self.get_date(), self.get_status(), self.get_id()]

    def __str__(self):
        return f"[TITLE]\n{self.title}\n[DESCRIPTION]\n{self.description}\n[DATE]\n{self.date}\n[STATUS]\n{self.status}"



