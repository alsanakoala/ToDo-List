import os
import json
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from plyer import notification
import tkinter as tk
from tkinter import messagebox, ttk
import winsound  # For sound notifications on Windows
import matplotlib.pyplot as plt  # For task analysis and graphs
from tkinter.simpledialog import askstring  # For setting goals

# User Class
# Created by: alsanakoala
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.task_manager = TaskManager()

# Task Class
# Created by: alsanakoala
class Task:
    def __init__(self, name, category, priority, due_date):
        self.name = name
        self.category = category
        self.priority = priority
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = False
        self.recurring = None

    def mark_complete(self):
        self.completed = True

    def postpone_task(self, days):
        self.due_date += timedelta(days=days)

    def set_recurring(self, interval_days):
        self.recurring = interval_days

    def update_recurring(self):
        if self.recurring and self.completed:
            self.due_date += timedelta(days=self.recurring)
            self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return (f"Task: {self.name} | Category: {self.category} | "
                f"Priority: {self.priority} | Status: {status} | "
                f"Due Date: {self.due_date.strftime('%Y-%m-%d')}")

# Task Manager Class
# Created by: alsanakoala
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.name}' added successfully.")

    def remove_task(self, task_name):
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.name != task_name]
        if len(self.tasks) < initial_count:
            print(f"Task '{task_name}' removed successfully.")
        else:
            print(f"Task '{task_name}' not found.")

    def filter_tasks(self, filter_by):
        if filter_by == "priority":
            return sorted(self.tasks, key=lambda task: task.priority)
        elif filter_by == "category":
            return sorted(self.tasks, key=lambda task: task.category)
        elif filter_by == "completed":
            return [task for task in self.tasks if task.completed]
        elif filter_by == "not completed":
            return [task for task in self.tasks if not task.completed]
        else:
            return self.tasks

    def get_statistics(self):
        total_tasks = len(self.tasks)
        completed_tasks = len([task for task in self.tasks if task.completed])
        incomplete_tasks = total_tasks - completed_tasks
        return total_tasks, completed_tasks, incomplete_tasks

    def backup_tasks(self, filename="backup.json"):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file, default=str)
        print(f"Tasks backed up to '{filename}'.")

    def restore_tasks(self, filename="backup.json"):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**data) for data in tasks_data]
            print(f"Tasks restored from '{filename}'.")
        except Exception as e:
            print(f"Error occurred while loading backup: {e}")

# Sound Notification Function (for Windows)
# Created by: alsanakoala
def play_sound():
    winsound.Beep(1000, 500)  # Beep sound at 1000 Hz for 500 ms

# Reminder Function
# Created by: alsanakoala
def show_reminder(task):
    notification.notify(
        title="Task Reminder",
        message=f"The task '{task.name}' is due soon ({task.due_date.strftime('%Y-%m-%d')}).",
        timeout=10
    )
    play_sound()  # Play a sound notification

def check_reminders(task_manager):
    today = datetime.now()
    for task in task_manager.tasks:
        if not task.completed and (task.due_date - today).days <= 1:
            show_reminder(task)

# Secure Email Notification Function
# Created by: alsanakoala
def send_secure_email_notification(to_email, subject, message):
    from_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Graphical Interface (tkinter)
# Created by: alsanakoala
class ToDoApp:
    def __init__(self, root, task_manager):
        self.root = root
        self.task_manager = task_manager

        # Window title and size
        self.root.title("Advanced To-Do List")
        self.root.geometry("800x800")
        self.root.configure(bg="#f0f8ff")

        # Title Label
        self.title_label = tk.Label(root, text="Advanced To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f8ff")
        self.title_label.pack(pady=10)

        # Input Frame
        self.input_frame = tk.Frame(root, bg="#e6f7ff", padx=10, pady=10)
        self.input_frame.pack(pady=10, fill="x")

        # Task Name
        self.task_name_label = tk.Label(self.input_frame, text="Task Name:", font=("Arial", 10), bg="#e6f7ff")
        self.task_name_label.grid(row=0, column=0, sticky="w")
        self.task_name_entry = tk.Entry(self.input_frame, width=40)
        self.task_name_entry.grid(row=0, column=1, pady=5)

        # Category
        self.category_label = tk.Label(self.input_frame, text="Category:", font=("Arial", 10), bg="#e6f7ff")
        self.category_label.grid(row=1, column=0, sticky="w")
        self.category_entry = tk.Entry(self.input_frame, width=40)
        self.category_entry.grid(row=1, column=1, pady=5)

        # Priority
        self.priority_label = tk.Label(self.input_frame, text="Priority (High/Medium/Low):", font=("Arial", 10), bg="#e6f7ff")
        self.priority_label.grid(row=2, column=0, sticky="w")
        self.priority_entry = tk.Entry(self.input_frame, width=40)
        self.priority_entry.grid(row=2, column=1, pady=5)

        # Due Date
        self.due_date_label = tk.Label(self.input_frame, text="Due Date (YYYY-MM-DD):", font=("Arial", 10), bg="#e6f7ff")
        self.due_date_label.grid(row=3, column=0, sticky="w")
        self.due_date_entry = tk.Entry(self.input_frame, width=40)
        self.due_date_entry.grid(row=3, column=1, pady=5)

        # Button Frame (Definition and Placement)
        self.button_frame = tk.Frame(root, bg="#f0f8ff", pady=10)
        self.button_frame.pack()

        # Add Task Button
        self.add_task_button = ttk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=0, padx=10)

        # List Tasks Button
        self.list_tasks_button = ttk.Button(self.button_frame, text="List Tasks", command=self.list_tasks)
        self.list_tasks_button.grid(row=0, column=1, padx=10)

        # Filter Options
        self.filter_option = tk.StringVar()
        self.filter_option.set("All")
        self.filter_menu = ttk.Combobox(self.button_frame, textvariable=self.filter_option, values=["All", "priority", "category", "completed", "not completed"])
        self.filter_menu.grid(row=0, column=2, padx=10)

        # Filter Button
        self.filter_button = ttk.Button(self.button_frame, text="Filter", command=self.filter_tasks)
        self.filter_button.grid(row=0, column=3, padx=10)

        # Toggle Theme Button
        self.theme_button = ttk.Button(self.button_frame, text="Toggle Theme", command=self.toggle_theme)
        self.theme_button.grid(row=1, column=0, pady=10, columnspan=2)

        # Show Statistics Button
        self.stats_button = ttk.Button(self.button_frame, text="Show Statistics", command=self.show_statistics)
        self.stats_button.grid(row=1, column=2, pady=10, columnspan=2)

        # Set Goal Button
        self.set_goal_button = ttk.Button(self.button_frame, text="Set Goal", command=self.set_goal)
        self.set_goal_button.grid(row=2, column=0, pady=10, columnspan=4)

        # Postpone Task
        self.days_label = tk.Label(root, text="Postpone Days:", font=("Arial", 10), bg="#f0f8ff")
        self.days_label.pack()
        self.days_entry = tk.Entry(root, width=10)
        self.days_entry.pack()

        self.postpone_button = ttk.Button(root, text="Postpone Task", command=self.postpone_task)
        self.postpone_button.pack(pady=10)

    # Method to add a new task
    # Created by: alsanakoala
    def add_task(self):
        name = self.task_name_entry.get()
        category = self.category_entry.get()
        priority = self.priority_entry.get()
        due_date = self.due_date_entry.get()

        try:
            task = Task(name, category, priority, due_date)
            self.task_manager.add_task(task)
            messagebox.showinfo("Success", "Task added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
    
    # Method to list all tasks
    def list_tasks(self):
        tasks_str = "\n".join(str(task) for task in self.task_manager.tasks)
        messagebox.showinfo("Tasks", tasks_str)

    # Method to filter tasks
    def filter_tasks(self):
        filter_by = self.filter_option.get()
        filtered_tasks = self.task_manager.filter_tasks(filter_by)
        tasks_str = "\n".join(str(task) for task in filtered_tasks)
        messagebox.showinfo("Filtered Tasks", tasks_str)

    # Method to toggle between light and dark theme
    def toggle_theme(self):
        if self.root.cget("bg") == "white":
            self.root.configure(bg="black")
            self.task_name_label.configure(bg="black", fg="white")
            # Update other components to match dark theme
        else:
            self.root.configure(bg="white")
            self.task_name_label.configure(bg="white", fg="black")
            # Update other components to match light theme

    # Method to show task statistics
    def show_statistics(self):
        total, completed, incomplete = self.task_manager.get_statistics()
        messagebox.showinfo("Statistics", f"Total Tasks: {total}\nCompleted: {completed}\nIncomplete: {incomplete}")

    # Method to postpone a task
    def postpone_task(self):
        task_name = self.task_name_entry.get()
        days = int(self.days_entry.get())
        for task in self.task_manager.tasks:
            if task.name == task_name:
                task.postpone_task(days)
                messagebox.showinfo("Success", f"Task '{task_name}' postponed by {days} days.")
                return
        messagebox.showerror("Error", f"Task '{task_name}' not found.")

    # Method to set a weekly goal
    def set_goal(self):
        goal = askstring("Set Goal", "Enter your weekly task goal:")
        if goal:
            messagebox.showinfo("Goal", f"Your weekly goal is: {goal} tasks")

# Main Program
# Created by: alsanakoala
# Created by: alsanakoala
if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager()
    app = ToDoApp(root, task_manager)
    root.mainloop()

    # Check reminders before exiting the program
    check_reminders(task_manager)
