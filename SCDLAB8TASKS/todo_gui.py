# todo_gui.py
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Initialize main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x350")

# Input box to enter a task
task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=10)

# "Add Task" button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# "Delete Task" button
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# A listbox showing current tasks
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

root.mainloop()