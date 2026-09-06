# Here we write the code that is work on, fonts, minimum screen(window) size, window title, custom font, label(text), config method of lable(used to change font), 


import tkinter as tk # you can also write like this
import tkinter.font as tfont
window = tk.Tk() # here Tk() is a class of tkinter module.

# so anything that we want to do, we have to write in between this right here before the mainloop. 

# window.mainloop()  # mainloop() function or method helps us to see the window and keeps it open, untill we close it back.

# window = tkinter.Tk() # can also be written as : tk.Tk() , if you define tkinter as tk at starting.

# title() : used to set title for the window 

window.title("My First App")
window.minsize(height=400, width=600) # It will set default height and width for the 

# # There is a second method to change font style of the text, There is a font class which basically sets the font and then we can use that font object created using the font class in my label class as a font argument.
custom_font = tfont.Font(family="Times New Roman", size=15, weight="bold")

# label = tkinter.Label(text="Hello everyone ! My name is Ayush\nHave a nice day dear.",font=("calibri",20,"bold"))
# # here in Label class we define text, its font, its font size, its weight. This all details are defined as tuple and stored in the font.
label = tk.Label(text="Hello Ayush\nI am pro of all time",font=custom_font)

label.pack() # this pack() method is used to bring any component to the window. if you not write this statement the screen will not show anything, the screen will be blank.

# # The window will automatically adjusted according to the text width and height.
# # so we can manually resize the window by using a method called minSize(). This function take values as pixels.

# # ========================================

# There is a socond method to change the font, after the lable creation is done.

label2 = tk.Label(text="I am Iron Man")
label2.pack(side="right", expand=True) # possible values of side : left, right, top(defaut value), bottom | the 'expand=True' is used to set text at the center on the window.
label2.config(font=("Courier New",25,"underline"))

window.mainloop()