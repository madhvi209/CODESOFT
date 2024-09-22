import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("To-Do List")
app.geometry("400x550")
app.config(bg="#1e1e2f")

font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 12, 'bold')

def add_task():
    task = task_entry.get("1.0", tk.END).strip()
    if task:
        # Prepend a circle (•) or square (■) symbol to the task
        styled_task = "• " + task  # Use "■ " for a square
        tasks_list.insert(tk.END, styled_task)
        task_entry.delete("1.0", tk.END)
    else:
        messagebox.showerror('Error', 'Enter a task.')

def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
    else:
        messagebox.showerror('Error', 'Choose a task to delete.')

def save_tasks():
    # Logic to save tasks to a file can be added here
    pass

# Title Label
title_label = tk.Label(app, font=font1, text="To-Do List", bg="#1e1e2f", fg="#ffffff")
title_label.place(x=80, y=20)

# Add Task Button
add_button = tk.Button(app, font=font2, text="Add Task", command=add_task, bg="#4CAF50", fg="white", borderwidth=0, padx=20, pady=10)
add_button.place(x=20, y=80)

# Remove Task Button
remove_button = tk.Button(app, font=font2, text="Remove Task", command=remove_task, bg="#f44336", fg="white", borderwidth=0, padx=20, pady=10)
remove_button.place(x=170, y=80)

# Task Entry
task_entry = tk.Text(app, height=2, width=24, font=("Arial", 18), bg="#ffffff", fg="#000000", borderwidth=2, relief="solid")
task_entry.place(x=40, y=150)

# Task List
tasks_list = tk.Listbox(app, width=35, height=15, font=font3, bg="#ffffff", fg="#000000", borderwidth=2, relief="solid")
tasks_list.place(x=40, y=230)

app.mainloop()
