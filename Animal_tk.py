import tkinter as tk    #importing the library for pop-up window
from tkinter import messagebox as mb 

def submit():

    global atype
    global aenv
    global afood
    

    atype = type_entry.get()
    aenv = env_entry.get()
    afood = food_entry.get()
    

    def string_check(a , b , c):                                                                    #checks if the inputed value is string; otherwise, gives message error pop-up
        if isinstance(a , str) == False  or isinstance(b , str) == False or isinstance(c , str) == False:
            mb.showerror("Invalid" , "Invalid")
            result = 0
            

        elif a.isspace() == True or b.isspace() == True or c.isspace() == True:                     #checks if the inputed value is only whitespace (any number)
            mb.showerror("Whitespaces" , "Whitespaces")
            result = 0
            

        elif a == "" or b == "" or c == "":                                                         #checks to see if there is no value whatsoever
            mb.showerror("emplystring" , "emptystring")
            result = 0
            

        else: 
            window.destroy()
            result = 1
            
        return print(result)
    
    string_check(atype , aenv , afood)

    
    
    
class Animal:
     
    def __init__(self, animalType, environment, food):
        self.animalType = animalType
        self.environment = environment
        self.food = food
        



window = tk.Tk()                             #initializez the creation of the GUI window
window.configure(bg = "#EFAEA1")             #sets the color of the backround to a light brown
window.geometry("400x200")                   #sets the size of the GUI window to 1000x800
window.title("Animals")                      #sets the title of the window to "Excel-Reader-Application"

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)


animal_type_label = tk.Label(window, text="Type:", bg="#C4A484") 
animal_type_label.grid(row=0, column=0, padx=5, pady=5, sticky="e") 

animal_env_label = tk.Label(window, text="Environment:", bg="#C4A484") 
animal_env_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

animal_food_label = tk.Label(window, text="Food:", bg="#C4A484")
animal_food_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

type_entry = tk.Entry(window)
type_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

env_entry = tk.Entry(window)
env_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

food_entry = tk.Entry(window)
food_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

result = 1

button_submit = tk.Button(window, text = "Submit" , command = submit)
button_submit.grid(row=4, column=0, columnspan=2, pady=5)

window.mainloop()                         #starts the pop-up for window

a = Animal(atype, aenv , afood)

full = f"The selected animal is a {atype} which lives in the {aenv} and eats {afood}."

#print("before if " + str(result)) #uncomment this to see the value of result just before the msg mainloop.

if result == 1:

    msg = tk.Tk()
    msg.configure(bg = "#EFAEA1")             #sets the color of the backround to a light brown
    msg.geometry("400x200")                   #sets the size of the GUI window to 1000x800
    msg.title("Message")

    msg_label = tk.Label(msg, text=full, bg="#C4A484") 
    msg_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")


    msg.mainloop()                            #starts the pop-up for msg









































































    





    
    