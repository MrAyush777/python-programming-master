import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Application")

my_frame = ttk.Frame()
my_frame.pack(side="left", fill="both", expand=True)

label1 = tk.Label(window, text="Hello World", bg="red")
label1.pack(side="top",fill="both", expand=True) # fill : possible values(both,none,x,y). Used to fill extra spaces reserved by an object(label1)

label2 = tk.Label(window, text="How are you ?", bg="blue")
label2.pack(side="top", fill="both", expand=True)

label3 = tk.Label(window, text="Have a nice day", bg="green")
label3.pack(side="top",fill="both", expand=True)


tk.mainloop()