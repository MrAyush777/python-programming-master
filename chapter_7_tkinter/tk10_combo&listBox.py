# import tkinter as tk
# import tkinter.ttk as ttk

# window = tk.Tk()
# window.title("Combobox & Listbox")

# # COMBOBOX

# selected_country = tk.StringVar()
# countries = ttk.Combobox(textvariable=selected_country, values=("India","US","UK","Australia"), state="readonly") 

# # By default if you not selected any value from the combobox, than you can able to write the value inside the combobox.
# # To restrict the user to write any value inside the combobox just write below statement :
# # countries["state"] = "readonly" # other method of give state="readonly"

# def display_country(event): # when event occurs the tkinter calls this function with that event as an argument 
#     country_label = tk.Label(text=selected_country.get())
#     country_label.pack()
#     print(f"selected country is {selected_country.get()}")

# # Here, now to just creating this function will not help us, and we don't able to use the command argument
# # Here we need to perform data binding. Here we have to bind this function to the combobox event.
# # Write a statement like below to bind the data :

# countries.bind("<<ComboboxSelected>>",display_country) # when this event happens(ComboboxSelected), this function(display_country) will be called and this event will be passed 

# countries.pack() 

# # =====================================================================================================


# # LISTBOX

# food_items = ("Pizza","Burger","Garlic Bread","Nachos","Salad")
# selected_food =  tk.StringVar(value=food_items)

# food_list = tk.Listbox(listvariable=selected_food, height=5, selectmode="extended")
# food_list.pack()

# def get_selected_food(event):
#     food_indices = food_list.curselection()
#     for i in food_indices:
#         print(food_list.get(i))
        
# food_list.bind("<<ListboxSelect>>",get_selected_food)

# tk.mainloop()



# =============================================================================================================================================================


import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

window.title("Combobox & Listbox")


# ============================================================
# COMBOBOX
# ============================================================

selected_country = tk.StringVar()

countries = ttk.Combobox(
    textvariable=selected_country,
    values=("India", "US", "UK", "Australia"),
    state="readonly"
)


def display_country(event):
    country_label.config(text=selected_country.get())

    print(f"selected country is {selected_country.get()}")


countries.bind("<<ComboboxSelected>>", display_country)

countries.pack()


country_label = tk.Label()
country_label.pack()


# ============================================================
# LISTBOX
# ============================================================

food_items = ("Pizza", "Burger", "Garlic Bread", "Nachos", "Salad")

selected_food = tk.StringVar(value=food_items)

food_list = tk.Listbox(
    listvariable=selected_food,
    height=5,
    selectmode="extended"
)

food_list.pack()


def get_selected_food(event):
    food_indices = food_list.curselection()

    for i in food_indices:
        print(food_list.get(i))


food_list.bind("<<ListboxSelect>>", get_selected_food)


# ============================================================

tk.mainloop()
