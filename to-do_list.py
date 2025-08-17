# A simple To-Do List application in Python

# We will use a list to store the tasks
tasks = []

def add_task(task_name):
  """Adds a new task to the to-do list."""
  tasks.append(task_name)
  print(f"Task '{task_name}' added successfully!")

def view_tasks():
  """Displays all tasks in the to-do list."""
  if not tasks:
    print("Your to-do list is empty.")
    return
  print("\n--- Your To-Do List ---")
  for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")
  print("----------------------\n")

def update_task(task_number, new_task_name):
  """Updates an existing task."""
  try:
    task_number = int(task_number)
    if 1 <= task_number <= len(tasks):
      tasks[task_number - 1] = new_task_name
      print(f"Task {task_number} updated to '{new_task_name}' successfully!")
    else:
      print("Invalid task number. Please try again.")
  except ValueError:
    print("Invalid input. Please enter a number.")

def delete_task(task_number):
  """Deletes a task from the list."""
  try:
    task_number = int(task_number)
    if 1 <= task_number <= len(tasks):
      removed_task = tasks.pop(task_number - 1)
      print(f"Task '{removed_task}' deleted successfully!")
    else:
      print("Invalid task number. Please try again.")
  except ValueError:
    print("Invalid input. Please enter a number.")

def main():
  """Main function to run the To-Do List application."""
  print("--- Welcome to the To-Do List Application! ---")
  while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
      task_name = input("Enter the task you want to add: ")
      add_task(task_name)
    elif choice == '2':
      view_tasks()
    elif choice == '3':
      view_tasks()
      task_number = input("Enter the number of the task to update: ")
      new_task_name = input("Enter the new task name: ")
      update_task(task_number, new_task_name)
    elif choice == '4':
      view_tasks()
      task_number = input("Enter the number of the task to delete: ")
      delete_task(task_number)
    elif choice == '5':
      print("Thank you for using the To-Do List application. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
  main()
