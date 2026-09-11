# Taking user input using Entry class
import tkinter as tk
from tkinter import *

window = tk.Tk()

def showText():
    inputedText = user_input.get()
    label.config(text=inputedText)
    
label = tk.Label(text="Hi guys !")
label.pack()

user_input = Entry(width=80)
# user_input.config(font=("calibri",18),bg="black",fg="white")
# user_input.insert(0,"fuck you...") # Text will automatically inserted when run this file...
# user_input.config(state="disabled") # It will disable the text field. It can have 3 possible values : disabled, normal and readonly
# user_input.config(width=40) # used to set the width of the text field (entry)
# user_input.config(show='*') # it means you write anything in the text field but it will show * each time.

user_input.pack()
print(user_input.get())

btn1 = tk.Button(text="Fuck You",command=showText)
btn1.pack()

tk.mainloop()