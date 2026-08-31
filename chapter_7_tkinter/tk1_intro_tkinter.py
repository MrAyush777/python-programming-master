# import tkinter
# import tkinter as tk # you can also write like this
# window = tkinter.Tk()

# window.mainloop()

import tkinter
import tkinter.font as tfont
window = tkinter.Tk()

window.title("My First App")
window.minsize(height=600, width=1000) # It will set default height and width for the 

# There is a second method to change font style of the text, There is a font class which basically sets the font and then we can use that font object created using the font class in my label class as a font argument.
custom_font = tfont.Font(family="Times New Roman",size=15, slant="italic", weight='bold')

label = tkinter.Label(text="Hello everyone ! My name is Ayush",font=custom_font)
# here in Label class we define text, its font, its font size, its weight. This all details are defined as tuple and stored in the font.

label.pack(side="left") # this pack() method is used to bring any component to the window.

# The window will automatically adjusted according to the text width and height.
# so we can manually resize the window by using a method called minSize(). This function take values as pixels.

# ========================================

label2 = tkinter.Label(text="I am Iron Man")
label2.pack()
label2.config(font=("Courier New",25))

window.mainloop()