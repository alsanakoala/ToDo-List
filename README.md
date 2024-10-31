# Advanced To-Do List Application

### Created by: alsanakoala

---

## Overview
The **Advanced To-Do List Application** is a comprehensive task management tool designed to help users organize and manage their tasks efficiently. With a user-friendly graphical interface built using `tkinter`, this application offers various features, including reminders, task filtering, goal setting, and more.

---

## Features
- **Task Management**: Add, remove, and postpone tasks with ease.
- **Task Filtering**: Filter tasks by priority, category, completion status, or view all tasks.
- **Reminders**: Receive notifications for tasks that are due soon, complete with sound alerts.
- **Secure Email Notifications**: Send email reminders using secure SMTP configuration.
- **Goal Setting**: Set and track weekly task goals.
- **Theme Switching**: Switch between light and dark modes for a personalized user experience.
- **Statistics**: View task statistics, including total tasks, completed tasks, and incomplete tasks.
- **Task Backup and Restore**: Backup tasks to a JSON file and restore them when needed.
- **Graphical Analysis**: Visualize task completion trends using graphs and charts (requires `matplotlib`).

---

## Installation
1. **Clone the Repository**: Download or clone the project to your local machine.
2. **Install Dependencies**:
   - Open a terminal or command prompt and run the following commands to install the required Python packages:
     ```bash
     pip install tkinter plyer matplotlib
     ```
3. **Configure Email**:
   - Set up your email environment variables `EMAIL_ADDRESS` and `EMAIL_PASSWORD` to enable secure email notifications.
   - You can set these variables in your operating system's environment settings.

---

## Usage
1. **Run the Application**:
   - Navigate to the project directory and run the script using:
     ```bash
     python <script_name>.py
     ```
   - Replace `<script_name>` with the name of your Python script file.

2. **Using the Application**:
   - **Add a Task**: Enter the task details (name, category, priority, due date) and click "Add Task".
   - **View Tasks**: Click "List Tasks" to see all tasks in a pop-up window.
   - **Filter Tasks**: Use the drop-down menu to filter tasks and click "Filter".
   - **Set a Goal**: Click "Set Goal" to set your weekly task goal.
   - **Toggle Theme**: Click "Toggle Theme" to switch between light and dark modes.
   - **View Statistics**: Click "Show Statistics" to see task statistics.
   - **Postpone Task**: Enter the number of days to postpone and click "Postpone Task".

3. **Reminders**:
   - The application will notify you of tasks that are due soon. Make sure sound notifications are enabled on your system for the best experience.

---

## Requirements
- **Python 3.7+**
- **Dependencies**:
  - `tkinter` (for GUI)
  - `plyer` (for notifications)
  - `matplotlib` (for graphs)
  - `smtplib` (for email notifications, built-in with Python)
  - `winsound` (for sound alerts on Windows)

---

## License
This project is open-source and available for personal and educational use.

---

## Author
- **alsanakoala**: The creator and maintainer of the Advanced To-Do List Application.

---

## Contributions
Feel free to contribute to this project! Fork the repository, make your changes, and submit a pull request.

---

## Future Improvements
- **Add recurring tasks**: Implement functionality for tasks that repeat on a schedule.
- **Mobile App**: Consider developing a mobile version of the application.
- **Integration with Calendar APIs**: Sync tasks with popular calendar services for better task management.

---

## Acknowledgments
Special thanks to all the open-source contributors and libraries that made this project possible.

---

### Notes
- Remember to set up your email settings properly to use the email notification feature.
- Feel free to modify and extend the project as per your needs!

