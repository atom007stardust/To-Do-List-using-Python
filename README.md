# Tkinter To-Do List Application
This is a simple To-Do List application created using Python's Tkinter library. The application allows users to add, delete, and list tasks in a graphical user interface (GUI).
## Features
Add Tasks: Enter a task in the input box and click "Add a new task" to add it to the list.
Delete Tasks: Select a task from the list and click "Delete a task" to remove it.
List Tasks: Click "List all tasks" to refresh and display all the current tasks.
Exit Application: Click "Exit" to close the application.

## Code Explanation
### Imports:

tkinter as tk: Provides the core Tkinter classes and methods.
tkinter.font: Used for custom font settings.
### Main Window Setup:

root = tk.Tk(): Initializes the main window.
root.title("My To-Do List"): Sets the window title.
root.geometry("400x500"): Defines the window size.
Task List:

tasks = []: Initializes an empty list to store tasks.
### Functions:

addTask(): Adds the task entered in the input box to the list.
deleteTask(): Removes the selected task from the list.
listTasks(): Displays all tasks in the list box.
exit(): Closes the application.
### UI Elements:

entry: Input box for new tasks.
button_frame: Frame to hold buttons.
add_button, delete_button, list_button, exit_button: Buttons for various actions.
list_box: Displays the list of tasks.
### Styling:

Custom fonts and button colors are used for a better visual appearance.
### Running the Application:

The main loop is started with root.mainloop(), which keeps the window open and responsive to user interactions.
