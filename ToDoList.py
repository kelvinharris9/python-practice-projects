# Define greeting function
def greeting():
    print("Hello.  Welcome to your to-do list.")

# Define function that will attempt to read file upon program executing
def load_tasks():
    # Attempt to open and read file
    try:
        with open("tasks.txt", "r") as f:
            # Return every task as an item in a list
            return [line.strip() for line in f.readlines()]
    # Return empty list if file does not exist
    except FileNotFoundError:
        return []

# Define function that displays to-do list to the user
def view_tasks(tasks):
    # Attempt to open and read file
    try:
        with open("tasks.txt", "r") as f:
            # If list is empty, notify user
            if not tasks:
                print("You have no tasks at this time.\n")
            # Otherwise, display tasks
            else:
                print("To-Do List")
                print("__________________________\n")
                for line in f.readlines():
                    print(f"{line.strip()}\n")
    # Notify user if file is not found
    except FileNotFoundError:
        print("File not found.\n")

# Define function that adds tasks to the list
def add_task(tasks):
    # Read in task as user input
    new_task = input("Enter the task you would like to add.\n"
                     "Type here -> ").strip()
    print("\n")
    # Add task to Python list
    tasks.append(f"-> {new_task}")
    # Overwrite .txt file with contents of Python list
    save_tasks(tasks)

# Define function that deletes tasks from the list
def delete_task(tasks):
    # If the list is not empty, display numbered to-do list
    if tasks:
        print("Here is your to-do list.\n")
        with open("tasks.txt", "r") as f:
            i = 1
            for line in f.readlines():
                print(f"{i}) {line[2:].strip()}")
                i += 1
        print("\n")
        # Read in corresponding int of task to delete as user input
        task_to_delete = int(input("Which task would you like to delete?\n"
                                   "Type the number here -> "))
        print("\n")
        # Delete task (converting from 1-based index
        # to  0-based index)
        tasks.pop(task_to_delete - 1)
        # Overwrite .txt file with contents of tasks list
        save_tasks(tasks)
    # If list is empty, notify user
    if not tasks:
        print("You have no tasks at this time.\n")

# Define function to overwrite .txt file with contents of tasks list
def save_tasks(tasks):
    # Open file in write mode; create file if it does not exist
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

# Define function to display menu to user
def menu():
    tasks = load_tasks()
    while True:
        # Display menu choices to user and read in input
        user_choice = input("What would you like to do?\n"
              "1) Add a task\n"
              "2) View tasks\n"
              "3) Delete a task\n"
              "4) Quit\n\n"
              "Type here -> ").strip()
        print("\n")
        # Call corresponding function of user choice
        if user_choice == "1":
            add_task(tasks)
        elif user_choice == "2":
            view_tasks(tasks)
        elif user_choice == "3":
            delete_task(tasks)
        elif user_choice == "4":
            exit()
        else:
            print("Invalid entry.  Please try again.")

# Define main function
def main():
    greeting()
    menu()

# Run the program only if this file is executed directly, not imported as a module
if __name__ == "__main__":
    main()