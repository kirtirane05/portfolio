import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")

tasks = []

def add_task(): 
    task = entry_task.get()
    if task != "":
        tasks.append(task)
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task)
        tasks.pop(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_all():
    listbox_tasks.delete(0, tk.END)
    tasks.clear()


frame = tk.Frame(root)
frame.pack(pady=10)

listbox_tasks = tk.Listbox(frame, height=15, width=45, selectmode=tk.SINGLE)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=35)
entry_task.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", width=15, command=add_task)
btn_add.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Task", width=15, command=delete_task)
btn_delete.pack(pady=5)

btn_clear = tk.Button(root, text="Clear All", width=15, command=clear_all)
btn_clear.pack(pady=5)

root.mainloop()
