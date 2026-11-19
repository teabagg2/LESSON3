import tkinter as tk
from tkinter import messagebox

# ---------- Main window ----------
root = tk.Tk()
root.title("ATM PIN Setup Interface")
root.geometry("500x700")
root.resizable(False, False)
root.config(bg="#e8eef5")

tk.Label(root, text="ATM PIN Setup", font=("Arial", 20, "bold"),
         bg="#e8eef5", fg="#1f3b57").pack(pady=(15, 5))

# ---------- Frame 1: account details (raised border, widgets placed with place()) ----------
account_frame = tk.Frame(root, width=450, height=190, bd=5, relief=tk.RAISED, bg="#ffffff")
account_frame.pack(padx=20, pady=10)
account_frame.pack_propagate(False)

tk.Label(account_frame, text="Account Details", font=("Arial", 13, "bold"),
         bg="#ffffff").place(x=10, y=5)

tk.Label(account_frame, text="Account Name:", bg="#ffffff").place(x=20, y=45)
name_entry = tk.Entry(account_frame, width=28)
name_entry.place(x=140, y=45)

tk.Label(account_frame, text="Account Number:", bg="#ffffff").place(x=20, y=85)
number_entry = tk.Entry(account_frame, width=28)
number_entry.place(x=140, y=85)

tk.Label(account_frame, text="Enter PIN (4 digits):", bg="#ffffff").place(x=20, y=125)
pin_entry = tk.Entry(account_frame, width=28, show="*")  # hides the PIN
pin_entry.place(x=140, y=145)

# ---------- Frame 2: keypad (sunken border, buttons placed with grid()) ----------
keypad_frame = tk.Frame(root, bd=5, relief=tk.SUNKEN, bg="#d5dde6", padx=10, pady=10)
keypad_frame.pack(padx=20, pady=10)


def press(digit):
    if len(pin_entry.get()) < 4:
        pin_entry.insert(tk.END, digit)


def clear_pin():
    pin_entry.delete(0, tk.END)


def backspace():
    pin_entry.delete(len(pin_entry.get()) - 1, tk.END)


keys = [
    ("1", 0, 0), ("2", 0, 1), ("3", 0, 2),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
]
for text, r, c in keys:
    tk.Button(keypad_frame, text=text, width=6, height=2, font=("Arial", 12, "bold"),
              command=lambda t=text: press(t)).grid(row=r, column=c, padx=4, pady=4)

tk.Button(keypad_frame, text="Clear", width=6, height=2, bg="#f4b0b0",
          command=clear_pin).grid(row=3, column=0, padx=4, pady=4)
tk.Button(keypad_frame, text="0", width=6, height=2, font=("Arial", 12, "bold"),
          command=lambda: press("0")).grid(row=3, column=1, padx=4, pady=4)
tk.Button(keypad_frame, text="Del", width=6, height=2, bg="#f4d9a0",
          command=backspace).grid(row=3, column=2, padx=4, pady=4)

# ---------- Frame 3: output (groove border) ----------
output_frame = tk.Frame(root, bd=4, relief=tk.GROOVE, bg="#ffffff")
output_frame.pack(padx=20, pady=10)

output_text = tk.Text(output_frame, width=48, height=6, state="disabled", bg="#f9f9f9")
output_text.pack(padx=5, pady=5)


# ---------- Submit button: reads the entered details and updates the Text widget ----------
def submit():
    name = name_entry.get().strip()
    number = number_entry.get().strip()
    pin = pin_entry.get()

    if not name or not number or not pin:
        messagebox.showwarning("Missing Details", "Please fill in all fields.")
        return
    if not number.isdigit():
        messagebox.showerror("Invalid Account Number", "Account number must contain digits only.")
        return
    if len(pin) != 4 or not pin.isdigit():
        messagebox.showerror("Invalid PIN", "PIN must be exactly 4 digits.")
        return

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END,
                       f"PIN setup successful!\n\n"
                       f"Account Name:   {name}\n"
                       f"Account Number: {number}\n"
                       f"PIN:            {'*' * len(pin)}\n")
    output_text.config(state="disabled")


tk.Button(root, text="Set PIN", font=("Arial", 13, "bold"), bg="#2e7d32", fg="white",
          width=15, command=submit).pack(pady=8)

root.mainloop()