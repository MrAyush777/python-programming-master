import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Text, Separator and Padding") 

# =================================================================================
# padding in tkinter

# 2 ways to give padding :

# method 1 : using padding argument
label1 = ttk.Label(text="Hello World !", padding=40) # It will give padding 40 pixel to label1, horizontally and vertically

# method 2 : using axies(x,y)
label1.pack(padx=30, pady=10) # pady will give padding before and after

sep1 = ttk.Separator(orient="horizontal")
sep1.pack(fill="x")

# =================================================================================

text = tk.Text(height=5, width=25)  # The one comment box will appear with width of 5 and height of 25 
text.pack(pady=30)

# text.focus() # by default when the window will appear the curser will blink in this text box.
text.insert("2.2","Enter your comments here") # it will enter text bydefault in this textbox. here 1 means first line , and 0 meand first characater.
# text.config(state="disabled") # It will disable the textbox.
text["state"] = "disabled"


# =================================================================================

# You can also enable the disabled components like below :

def enableTextBox():
    text["state"] = "normal"
    

enable_button = tk.Button(text="Enable Text Box", bg="black", fg="white", command=enableTextBox)
enable_button.pack()

# ==================================================================================

sep2 = ttk.Separator(orient="horizontal")
sep2.pack(fill="x")

# ==================================================================================
# get() method : The get() method is used to retrieve the current value or text from a widget. It's behaviour depends on widget type.



# below part : it will get text from the text box and print it in the console.
def getTextData():
    textData = text.get("1.0","end")
    print(textData)

get_text = ttk.Button(text="Get Text", command=getTextData)
get_text.pack()






tk.mainloop()