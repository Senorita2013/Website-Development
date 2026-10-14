import tkinter as tk
from tkinter import messagebox

def open_planner():
    window = tk.Toplevel(root)
    window.title("Reading Planner")
    window.geometry("300x280")

    tk.Label(window, text="Total book pages:").pack(pady=5)
    total_entry = tk.Entry(window)
    total_entry.pack()

    tk.Label(window, text="Pages per day:").pack(pady=5)
    daily_entry = tk.Entry(window)
    daily_entry.pack()

    result = tk.Label(window, text="")
    result.pack(pady=15)

    def calculate():
        try:
            total = int(total_entry.get())
            daily = int(daily_entry.get())

            if total <= 0 or daily <= 0:
                raise ValueError

            complete_days = total // daily
            remaining_pages = total % daily

            days = complete_days + (1 if remaining_pages else 0)

            result.config(
                text=f"Complete days: {complete_days}\n"
                     f"Remaining pages: {remaining_pages}\n"
                     f"Total reading days: {days}"
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Enter positive whole numbers."
            )

    tk.Button(window, text="Calculate", command=calculate).pack()


root = tk.Tk()
root.title("Reading Schedule Planner")
root.geometry("300x180")

tk.Label(
    root,
    text=" Reading Schedule Planner",
    font=("Arial", 14, "bold")
).pack(pady=20)

tk.Button(
    root,
    text="Open Planner",
    command=open_planner
).pack()

root.mainloop()