import tkinter as tk


class ToDoList:
    def __init__(self):
        self.tasks = []
        self.task_number = 1

        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.title("To-Do List App")

        self.task_entry = tk.Entry(self.window, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        self.add_task_btn = tk.Button(self.window, text="Add Task", command=self.add_task)
        self.add_task_btn.grid(row=0, column=1, padx=5, pady=5)

        self.task_list_box = tk.Listbox(self.window, width=40)
        self.task_list_box.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.task_list_box.bind("<Double-Button-1>", self.remove_task)

        self.remove_task_btn = tk.Button(self.window, text="Remove Task", command=self.remove_selected_task)
        self.remove_task_btn.grid(row=2, column=0, padx=5, pady=5)

        self.clear_all_tasks_btn = tk.Button(self.window, text="Clear All Tasks", command=self.clear_all_tasks)
        self.clear_all_tasks_btn.grid(row=2, column=1, padx=5, pady=5)

        self.load_tasks()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list_box.insert(tk.END, f"{self.task_number}. {task}")
            self.task_number += 1
            self.task_entry.delete(0, tk.END)

    def remove_task(self, event):
        task_index = self.task_list_box.curselection()[0]
        self.task_list_box.delete(task_index)
        self.tasks.pop(task_index)
        self.task_number -= 1
        for i in range(task_index, self.task_number):
            self.task_list_box.delete(i)
            self.task_list_box.insert(i, f"{i + 1}. {self.tasks[i]}")

    def remove_selected_task(self):
        selected_task_index = self.task_list_box.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.task_list_box.delete(task_index)
            self.tasks.pop(task_index)
            self.task_number -= 1
            for i in range(task_index, self.task_number):
                self.task_list_box.delete(i)
                self.task_list_box.insert(i, f"{i + 1}. {self.tasks[i]}")

    def clear_all_tasks(self):
        self.task_list_box.delete(0, tk.END)
        self.tasks.clear()
        self.task_number = 1

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            f.write("\n".join(self.tasks))

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.read().splitlines()
            for task in tasks:
                self.tasks.append(task)
                self.task_list_box.insert(tk.END, f"{self.task_number}. {task}")
                self.task_number += 1
        except FileNotFoundError:
            pass

    def on_closing(self):
        self.save_tasks()
        self.window.destroy()


ToDoList()
