import tkinter as tk
from tkinter import messagebox

# ---------- Main window ----------
root = tk.Tk()
root.title("After-School Routine Checker")
root.geometry("520x560")
root.resizable(False, False)
root.config(bg="#eef3e8")

# Starting routine (new tasks you add get appended to this list)
routine = ["Change out of uniform", "Eat a snack", "Do homework", "Read a book", "Pack school bag"]
current_index = -1  # -1 means no task shown yet

tk.Label(root, text="After-School Routine Checker", font=("Arial", 18, "bold"),
         bg="#eef3e8", fg="#2e4a1f").pack(pady=(15, 10))

# ---------- Task entry (keyboard events) ----------
tk.Label(root, text="Type a task:", font=("Arial", 12), bg="#eef3e8").pack()
task_entry = tk.Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=5)

last_key_label = tk.Label(root, text="Last character typed: -", font=("Arial", 12),
                          bg="#eef3e8", fg="#1f3b57")
last_key_label.pack(pady=5)


def on_key_press(event):
    """Show the last character the user typed."""
    if event.char and event.char.isprintable():
        shown = event.char
    else:
        shown = f"[{event.keysym}]"  # special keys like BackSpace, Shift
    last_key_label.config(text=f"Last character typed: {shown}")


task_entry.bind("<KeyPress>", on_key_press)

# ---------- Routine area (mouse click event) ----------
tk.Label(root, text="Click the routine area:", font=("Arial", 12), bg="#eef3e8").pack(pady=(10, 0))

routine_area = tk.Frame(root, width=420, height=110, bd=4, relief=tk.RIDGE, bg="#fff8dc")
routine_area.pack(pady=5)
routine_area.pack_propagate(False)

routine_label = tk.Label(routine_area, text="Routine area - click me!", font=("Arial", 12),
                         bg="#fff8dc")
routine_label.pack(expand=True)

colors = ["#fff8dc", "#d6f5d6", "#d6e6f5", "#f5d6e6"]
click_count = 0


def on_click(event):
    """React to a mouse click inside the routine area."""
    global click_count
    click_count += 1
    new_color = colors[click_count % len(colors)]
    routine_area.config(bg=new_color)
    routine_label.config(bg=new_color,
                         text=f"Clicked at ({event.x}, {event.y})  |  Clicks: {click_count}")


routine_area.bind("<Button-1>", on_click)
routine_label.bind("<Button-1>", on_click)

# ---------- Warning + next task display ----------
status_label = tk.Label(root, text="", font=("Arial", 11, "bold"), bg="#eef3e8", fg="red")
status_label.pack(pady=5)

next_task_label = tk.Label(root, text="Next task: press the button below",
                           font=("Arial", 14, "bold"), bg="#eef3e8", fg="#2e4a1f",
                           wraplength=460)
next_task_label.pack(pady=5)


def add_task():
    task = task_entry.get().strip()
    if not task:
        # Warning when no task is entered
        status_label.config(text="Warning: please enter a task first!", fg="red")
        messagebox.showwarning("No Task Entered", "Please type a task before adding it.")
        return
    routine.append(task)
    task_entry.delete(0, tk.END)
    last_key_label.config(text="Last character typed: -")
    status_label.config(text=f"Added: {task}", fg="green")


def next_task():
    global current_index
    if not routine:
        next_task_label.config(text="Your routine is empty!")
        return
    current_index = (current_index + 1) % len(routine)
    next_task_label.config(text=f"Next task: {routine[current_index]}")
    status_label.config(text=f"Task {current_index + 1} of {len(routine)}", fg="#1f3b57")


# ---------- Buttons ----------
button_frame = tk.Frame(root, bg="#eef3e8")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", width=14, font=("Arial", 12, "bold"),
          bg="#2e7d32", fg="white", command=add_task).grid(row=0, column=0, padx=8)
tk.Button(button_frame, text="Next Task", width=14, font=("Arial", 12, "bold"),
          bg="#1565c0", fg="white", command=next_task).grid(row=0, column=1, padx=8)

root.mainloop()