from tkinter import *
from datetime import date

root = Tk()

root.title("hello tkinter")
root.geometry("400x450")

lbl = Label(root, text = "Hey There!", fg = "white", bg = "blue", height = 1, width = 300)
name_lbl = Label(root, text = "Enter your full name:", bg = "lightblue")

font = ("Times New Roman", 14)

name_entry = Entry(root, font = font)

def display():
    name = name_entry.get()
    global message 
    message = "Welcome to the Application, today's date is:"
    greet = "Hello " + name + "!"
    
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
    text_box.insert(END, "\n")
    
    
text_box = Text(height = 3, font = font)

btn = Button(text = "Begin", command = display, height = 1)
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()

    