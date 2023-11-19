import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from datetime import datetime

class HealthWellnessPlatform:
    def __init__(self, master):
        self.master = master
        master.title("Health and Wellness Platform")

        # Initialize database
        self.conn = sqlite3.connect('health_data.db')
        self.create_table()

        # Initialize GUI components
        self.label_date = Label(master, text="Date:")
        self.label_steps = Label(master, text="Steps:")
        self.label_water_intake = Label(master, text="Water Intake (ml):")
        self.label_sleep_duration = Label(master, text="Sleep Duration (hours):")

        self.entry_date = Entry(master)
        self.entry_steps = Entry(master)
        self.entry_water_intake = Entry(master)
        self.entry_sleep_duration = Entry(master)

        self.submit_button = Button(master, text="Submit", command=self.record_health_data)
        self.view_button = Button(master, text="View Health Data", command=self.view_health_data)

        # Place GUI components
        self.label_date.grid(row=0, column=0)
        self.label_steps.grid(row=1, column=0)
        self.label_water_intake.grid(row=2, column=0)
        self.label_sleep_duration.grid(row=3, column=0)

        self.entry_date.grid(row=0, column=1)
        self.entry_steps.grid(row=1, column=1)
        self.entry_water_intake.grid(row=2, column=1)
        self.entry_sleep_duration.grid(row=3, column=1)

        self.submit_button.grid(row=4, column=0, columnspan=2)
        self.view_button.grid(row=5, column=0, columnspan=2)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS health_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                steps INTEGER,
                water_intake INTEGER,
                sleep_duration REAL
            )
        ''')
        self.conn.commit()

    def record_health_data(self):
        date = self.entry_date.get()
        steps = self.entry_steps.get()
        water_intake = self.entry_water_intake.get()
        sleep_duration = self.entry_sleep_duration.get()

        if not (date and steps and water_intake and sleep_duration):
            messagebox.showinfo("Input Error", "Please fill in all fields.")
            return

        try:
            steps = int(steps)
            water_intake = int(water_intake)
            sleep_duration = float(sleep_duration)
        except ValueError:
            messagebox.showinfo("Input Error", "Invalid input. Steps and water intake should be integers, and sleep duration should be a number.")
            return

        self.conn.execute('''
            INSERT INTO health_data (date, steps, water_intake, sleep_duration)
            VALUES (?, ?, ?, ?)
        ''', (date, steps, water_intake, sleep_duration))

        self.conn.commit()
        messagebox.showinfo("Success", "Health data recorded successfully.")

    def view_health_data(self):
        cursor = self.conn.execute("SELECT * FROM health_data")
        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo("No Data", "No health data recorded.")
            return

        result_str = "Health Data Summary:\n"
        for row in rows:
            result_str += f"ID: {row[0]}, Date: {row[1]}, Steps: {row[2]}, Water Intake: {row[3]} ml, Sleep Duration: {row[4]} hours\n"

        messagebox.showinfo("Health Data", result_str)

# Example usage
if __name__ == "__main__":
    root = Tk()
    platform = HealthWellnessPlatform(root)
    root.mainloop()