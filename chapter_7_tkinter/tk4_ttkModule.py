"""
ttk module : 
Themed Tk(Ttk) is a newer family of Tk widges that provide a much better appearance on different platforms than many of the classic Tk widges.

"""
# Taking user input using Entry class

import tkinter as tk
from tkinter import *
from tkinter import ttk 

window = tk.Tk()

def showText():
    inputedText = user_input.get()
    label.config(text=inputedText)
    
label = ttk.Label(text="Hi guys !")
label.pack()

user_input = ttk.Entry(width=80)

user_input.pack()
print(user_input.get())

btn1 = ttk.Button(text="Fuck You",command=showText)
btn1.pack()

tk.mainloop()