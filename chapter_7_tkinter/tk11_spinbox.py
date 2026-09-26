# spinbox : Is used to increase or decrese the values(usually integers) using arrow keys.

import tkinter as tk
from tkinter import ttk

window = tk.Tk() 

# by default when you run this, the spinbox will be completely blank.
# to set default value in it :
counter = tk.IntVar(value=10)

# spinbox = ttk.Spinbox(from_=0, to=20) # here 'from_' having underscor in its syntax, because the 'from' keyword has alread reserved. so defferentiate the underscore sign has added to use it differently here.
# There is also an argument called 'wrap' in the 'ttk.Spinbox()', it can have two values - True and False. its working is : when we reach the end(20) and then if we click down arrow than it will not stop, it will again start form 0. and same working when we reach to 0 and click upper arrow. By default its value is False. 
spinbox = ttk.Spinbox(from_=0, to=40, textvariable=counter) # it will set default value = 10 , when we run the app.
spinbox.pack()

# if you want to retrieve the value from the spinbox, you can use getI() method. But it will work only one time. Because the code is executed one time only. If you want that the value will saw each time it change, than you can get help of function. Also remember to use the command argument in the spinbox to call that function each time we change the value.

# In the spinbox we use from_ and to to specity the range of numbers. But you can decide the set of numbers in the spinbox, just use 'values' paramenter and write values in the tuple. Ex. values=(10,20,30,40) in the Spinbox() method.
# You also can set values using the range function. Ex. values=tuple(range(10,20,30,40,50))

tk.mainloop()

