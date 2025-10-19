from utils import *

def create_task():

    title = get_title()
    description = get_description()
    date = datetime.today().strftime('%Y-%m-%d')
    custom_id = generate_custom_id()

    task  = Task(title, description, date, custom_id).get_df()


    print(task)





create_task()
