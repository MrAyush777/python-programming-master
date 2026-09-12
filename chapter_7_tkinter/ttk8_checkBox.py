import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("CheckBoxes in Tkinter")

# check_option = tk.IntVar() # stores 0 or 1 values... as integers
check_option = tk.StringVar()  # stores string values... like,  "Yes" of "No"

def checkOptionTask():
    print(check_option.get())

check_button = ttk.Checkbutton(text="Agree with the terms and the conditions.", variable=check_option, command=checkOptionTask, onvalue="Yes", offvalue="No")
check_button.pack()

tk.mainloop()