# destroy method used to quit our application/window.

import tkinter as tk

window = tk.Tk()

window.title("Destroy")

label = tk.Label(text="It is a Tkinter module of the Python\n")
label.pack()


# when you click this button, the window will be closed.
quit_button = tk.Button(text="Quit",command=window.destroy)
quit_button.pack()

tk.mainloop()