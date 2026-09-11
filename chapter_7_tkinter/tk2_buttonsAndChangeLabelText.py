# This file is all about buttons, chage label text, 

import tkinter as tk
import tkinter.font as tfont

window = tk.Tk()
window.title("DemoPage")
window.minsize(height=400, width=600)

custome_font = tfont.Font(family="calibri", size=18, weight="bold")

label = tk.Label(text="This is sample file",font=custome_font)
label.pack()

# There are 2 methods for changing the text on to the screen :

# 1) method 1 :
label["text"] = "Have a nice day my dear friend"

# 2) method 2 : using config method. Config method is also used to change the paremeters or arguments of the label class. 
label.config(text="I am Iron Man")

# ===========================================

# Buttons : buttons are clickable component on the window.
count = 0
def prt():
    global count
    count += 1
    # print("Another Stuff...!")
    label.config(text=f"the button has clicked {count} times")

btn1 = tk.Button(text="Log in",command=prt)
btn1.pack()

tk.mainloop()