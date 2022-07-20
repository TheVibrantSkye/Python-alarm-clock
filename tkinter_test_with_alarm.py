from datetime import date
from datetime import datetime
from tkinter import *
from tkinter import ttk
import time
import threading

root = Tk() # noqa
root.title("Python Alarm!")
root.geometry("500x250")
root.iconbitmap(r'pocket watch.ico')
root['bg'] = 'black'


def create_window():
    win = Toplevel(root)
    win.geometry("500x250")
    win.title("Time type and preferences")

    yes_button = Button(win, text="Yes", padx=40, pady=20, bg="grey", fg="white")
    yes_button.grid(row=1, column=0)

    no_button = Button(win, text ="No", padx=40, pady=20, bg="grey", fg="white")
    no_button.grid(row=1, column=1)

start_program_button = Button(root, text='Start program', command=create_window, padx=40, pady=20, bg="grey", fg="white")
start_program_button.grid(row=1, column=0)

# e = Entry(root, width=35, borderwidth=5, bg="grey", fg="white")
# e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

test_label = Label(root, text='Welcome to my test!', bg="grey", fg="white")
test_label.grid(row=0, column=0)


def user_time_type():
    '''This function is designed purely to get the time format a user wants,
    while also containing built-in input validation
    so I don't have to write it in main.'''
    placeholder_state = True
    while placeholder_state == True: # noqa
        user_time_type_choice = input("Would you like the clock to be in 12 hour or 24 hour format? \n\n") # noqa

        if user_time_type_choice == "12":
            while True:
                user_time_type_confirmation = input("Is 12 hour format correct? y/n \n").lower() # noqa

                if user_time_type_confirmation == "y".lower():
                    print("\n12 hour format selected!")
                    placeholder_state = False
                    user_time_selection = 12
                    return user_time_selection

                elif user_time_type_confirmation == "n".lower():
                    print("\nBack to type selection!")
                    break

                else:
                    print("\nPlease enter y or n!")

        elif user_time_type_choice == "24":
            while True:
                user_time_type_confirmation = input("Is 24 hour format okay? y/n \n").lower() # noqa

                if user_time_type_confirmation == "y".lower():
                    print("\n24 hour format selected!")
                    placeholder_state = False
                    user_time_selection = 24
                    return user_time_selection

                elif user_time_type_confirmation == "n".lower():
                    print("\nBack to type selection!")
                    break

                else:
                    print("\nPlease enter y or n!")


root.mainloop()
