import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Radio Button in Tkinter")

radio_value = tk.StringVar()

def getRadioValue():
    print(radio_value.get())

option_1 = ttk.Radiobutton(text="Male", variable=radio_value, value="male", command=getRadioValue)
option_2 = ttk.Radiobutton(text="Female", variable=radio_value, value="female", command=getRadioValue)

option_1.pack()
option_2.pack()


tk.mainloop()