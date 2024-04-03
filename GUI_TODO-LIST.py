import tkinter as tk

class TodoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TodoListApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List App")

        self.todo_list = []

        self.title_label = tk.Label(master, text="To-Do List")
        self.title_label.pack()

        self.input_frame = tk.Frame(master)
        self.input_frame.pack()

        self.title_entry = tk.Entry(self.input_frame)
        self.title_entry.pack(side=tk.LEFT)
        self.title_entry.focus_set()

        self.description_entry = tk.Entry(self.input_frame)
        self.description_entry.pack(side=tk.LEFT)

        self.add_button = tk.Button(self.input_frame, text="Add", command=self.add_todo)
        self.add_button.pack(side=tk.LEFT)

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.remove_button = tk.Button(master, text="Remove", command=self.remove_todo)
        self.remove_button.pack()

        self.display_items()

    def add_todo(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        if title:
            self.todo_list.append(TodoItem(title, description))
            self.display_items()
            self.title_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)

    def remove_todo(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            del self.todo_list[index]
            self.display_items()

    def display_items(self):
        self.listbox.delete(0, tk.END)
        for item in self.todo_list:
            status = "Completed" if item.completed else "Not Completed"
            self.listbox.insert(tk.END, f"{item.title} - {item.description} ({status})")


def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
