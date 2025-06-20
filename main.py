from task_manager import (
    Task,
    show_tasks_no_info,
    update_task_in_list as update_task,
    select_task,
    update_status,
    show_info_task,
    safe_input,
    safe_int_input,
    load_tasks,
    save_tasks,
)

print("Press 'q' at any time to close the program.\n")

todo = load_tasks()


def get_user_input() -> int:
    print(
        f"Welcome to Task Manager\n"
        f"Options:\n"
        f"1) Add a new task\n"
        f"2) Update a task\n"
        f"3) Delete task\n"
        f"4) Show tasks overview\n"
        f"5) Show task details\n"
        f"{'-' * 60}"
    )
    while True:
        try:
            user_input = safe_int_input("Please select an option: ")
            if 1 <= user_input <= 5:
                return user_input
            else:
                print(f"Error: {user_input} is not between 1 and 5. Please try again.")
        except ValueError:
            print("Error: Please enter a valid number between 1 and 5.")


def do_todo():
    global todo
    while True:
        user_input = get_user_input()

        if user_input == 1:
            print("\nAdding a new task")
            title = safe_input("What are you going to do? ")
            info = safe_input("Please describe your task (optional): ")
            new_task = Task(title, info).get_data()
            todo.append(new_task)
            save_tasks(todo)
            print(f"\nTask '{title}' added successfully!")
            show_tasks_no_info(todo)

        elif user_input == 2:
            if not todo:
                print("\nThere are no tasks to update")
            else:
                print("\nUpdating a task")
                print("Options:\n1) Replace task content\n2) Toggle completion status")

                while True:
                    try:
                        option = safe_int_input("Please select an update option: ")
                        if option in (1, 2):
                            break
                        else:
                            print("Error: Please select 1 or 2.")
                    except ValueError:
                        continue

                options, index = select_task(todo)
                if index == -1:  # No tasks available
                    continue

                selected_task = todo[index]

                if option == 1:
                    print(f"\nReplacing task: {selected_task['title']}")
                    new_title = safe_input("What is the new task? ")
                    new_info = safe_input("Please describe the new task (optional): ")

                    # Crear nueva tarea manteniendo el mismo ID
                    updated_task = Task(
                        new_title,
                        new_info,
                        selected_task["completed"],
                        date=selected_task["date"],
                        task_id=selected_task["id"],
                    ).get_data()

                    update_task(todo, selected_task, updated_task)
                    save_tasks(todo)
                    print("\nTask replaced successfully!")

                elif option == 2:
                    update_status(selected_task)
                    save_tasks(todo)
                    new_status = (
                        "Completed" if selected_task["completed"] else "Pending"
                    )
                    print(f"\nTask status updated to: {new_status}")

                show_tasks_no_info(todo)

        elif user_input == 3:
            if not todo:
                print("\nThere are no tasks to delete")
            else:
                print("\nDeleting a task")
                options, index = select_task(todo)
                if index == -1:
                    continue

                deleted_title = todo[index]["title"]
                del todo[index]
                save_tasks(todo)
                print(f"\nTask '{deleted_title}' deleted successfully!")
                show_tasks_no_info(todo)

        elif user_input == 4:
            show_tasks_no_info(todo)

        elif user_input == 5:
            show_info_task(todo)

        # Pausa antes de volver al menú
        safe_input("\nPress Enter to return to the menu...")
        print("\n" + "=" * 60)


# Iniciar la aplicación
if __name__ == "__main__":
    do_todo()

