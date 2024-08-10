import tkinter as tk
from tkinter import font

#Create the main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x500") #Set window size


#Create an empty list to hold the tasks
tasks = []

#Function to add a task
def addTask():
    task =  entry.get()
    if task:  #if task is not empty
        tasks.append(task)
        list_box.insert(tk.END,task) #tk.END means task should be added at the end of the list, task indicates the content
        entry.delete(0,tk.END) #clear the entry box

def deleteTask():
    selected_task_index = list_box.curselection() #gets the index of the selected task
    #curselection returns a tuple of all the selected choices
    if selected_task_index:
        index=selected_task_index[0]
        tasks.pop(index)
        list_box.delete(index)
def listTasks():
    list_box.delete(0,tk.END)
    for index, task in enumerate(tasks):
        list_box.insert(tk.END,f"{index}. {task}")
def exit():
    root.quit()





#Additional styling
#Custom font
custom_font = font.Font(family="Arial",size=12)
#Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

#In GUI, a user doesn't interact through a console, rather they interact with text boxes
#so you need gui elements rather than input or print

#Create an entry box to enter new tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

#Now create a button for adding the tasks
add_button = tk.Button(button_frame, text = "Add a new task ", font=("Arial",18),command=addTask,bg="#4CAF50",fg="white")
add_button.grid(row=0,column=0,padx=5,pady=5)


#Creating a button for deleting tasks
delete_button = tk.Button(button_frame, text = "Delete a task", font=("Arial",18),command=deleteTask,bg="#F44336",fg="white")
delete_button.grid(row=0,column=1,padx=5,pady=5)

#Create a button for listing all the tasks
list_button = tk.Button(button_frame, text="List all tasks", font=("Arial",18),command=listTasks,bg="#2196F3",fg="white")
list_button.grid(row=1, column=0,padx=5,pady=5)

#Creating a list box to display a list of items
list_box = tk.Listbox(root, width=50,height=20,font=custom_font,selectmode=tk.SINGLE)
list_box.pack(pady=10)

#Create a button to exit the applicaiton
exit_button = tk.Button(button_frame, text="Exit", font= ("Arial",18),command=exit,bg="#FFC107",fg="black")
exit_button.grid(row=1, column=1,padx=5,pady=5)

#The Command Parameter:
#When you createa a button using tk.Button(), command parameter can be used to link it to a specific function, like(add a task, delete a task, list all tasks) etc
#The function listed in Command will be executed, whenever that button is pressed









#Run the window's main loop
root.mainloop()