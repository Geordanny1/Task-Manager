from task import Task
import pandas as pd
import os

TASK_FILE = "task_list.pkl"

def save_task(data_frame) -> None:
    """Save a new task to the task list"""
    if os.path.exists(TASK_FILE):
        existing_df = pd.read_pickle(TASK_FILE)
        combined_df = pd.concat([existing_df, data_frame], ignore_index=True)
        combined_df.to_pickle(TASK_FILE)
    else:
        data_frame.to_pickle(TASK_FILE)

def get_task_list():
    """Retrieve all tasks"""
    if not os.path.exists(TASK_FILE):
        return pd.DataFrame(columns=["TITLE", "DESCRIPTION", "DATE", "STATUS", "ID"])
    return pd.read_pickle(TASK_FILE)

def update_task(task_id, new_title=None, new_description=None, new_status=None):
    """Update a task by ID"""
    if not os.path.exists(TASK_FILE):
        print("\nNo tasks found in the system.")
        return False
    
    df = get_task_list()
    
    if df.empty:
        print("\nNo tasks found in the system.")
        return False
    
    # Find the task by ID
    task_mask = df['ID'] == task_id
    
    if not task_mask.any():
        print(f"\n✗ Task with ID '{task_id}' not found.")
        print("\nAvailable tasks:")
        show_available_tasks()
        return False
    
    # Update the fields that were provided
    if new_title:
        df.loc[task_mask, 'TITLE'] = new_title
    if new_description:
        df.loc[task_mask, 'DESCRIPTION'] = new_description
    if new_status:
        df.loc[task_mask, 'STATUS'] = new_status
    
    # Reset index before saving to avoid issues
    df = df.reset_index(drop=True)
    df.to_pickle(TASK_FILE)
    return True

def delete_task(task_id):
    """Delete a task by ID"""
    if not os.path.exists(TASK_FILE):
        print("\nNo tasks found in the system.")
        return False
    
    df = get_task_list()
    
    # Check if task exists
    if task_id not in df['ID'].values:
        print(f"\n✗ Task with ID '{task_id}' not found.")
        print("\nAvailable tasks:")
        show_available_tasks()
        return False
    
    # Remove the task
    df = df[df['ID'] != task_id]
    
    if df.empty:
        os.remove(TASK_FILE)
    else:
        df.to_pickle(TASK_FILE)
    
    return True

def list_tasks(status_filter=None):
    """List all tasks, optionally filtered by status"""
    df = get_task_list()
    
    if df.empty:
        print("No tasks found.")
        return
    
    if status_filter:
        df = df[df['STATUS'] == status_filter]
        if df.empty:
            print(f"No tasks with status '{status_filter}' found.")
            return
    
    print("\n" + "="*80)
    print(f"{'ID':<25} {'TITLE':<20} {'STATUS':<15} {'DATE':<12}")
    print("="*80)
    
    for _, row in df.iterrows():
        print(f"{row['ID']:<25} {row['TITLE'][:20]:<20} {row['STATUS']:<15} {row['DATE']:<12}")
    
    print("="*80)
    print(f"Total tasks: {len(df)}\n")

def view_task(task_id):
    """View detailed information about a specific task"""
    df = get_task_list()
    
    if df.empty:
        print("\nNo tasks found in the system.")
        return
    
    if task_id not in df['ID'].values:
        print(f"\n✗ Task with ID '{task_id}' not found.")
        print("\nAvailable tasks:")
        show_available_tasks()
        return
    
    task = df[df['ID'] == task_id].iloc[0]
    
    print("\n" + "="*80)
    print(f"[TITLE]\n{task['TITLE']}")
    print(f"\n[DESCRIPTION]\n{task['DESCRIPTION']}")
    print(f"\n[DATE]\n{task['DATE']}")
    print(f"\n[STATUS]\n{task['STATUS']}")
    print(f"\n[ID]\n{task['ID']}")
    print("="*80 + "\n")

def clear_all_tasks():
    """Delete all tasks"""
    if os.path.exists(TASK_FILE):
        os.remove(TASK_FILE)

def show_available_tasks():
    """Display a compact list of available tasks"""
    df = get_task_list()
    
    if df.empty:
        print("  (No tasks available)")
        return
    
    print("\n" + "-"*80)
    print(f"{'ID':<25} {'TITLE':<30} {'STATUS':<15}")
    print("-"*80)
    
    for _, row in df.iterrows():
        title = row['TITLE'][:27] + "..." if len(row['TITLE']) > 30 else row['TITLE']
        print(f"{row['ID']:<25} {title:<30} {row['STATUS']:<15}")
    
    print("-"*80)
    print("Tip: Copy the exact ID from above to use in your command.\n")
