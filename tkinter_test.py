from tkinter import *


root = Tk() # noqa
root.title("My calculator")
root.iconbitmap(r'C:\Users\Douglas Napier\Desktop\pocket watch.ico')

e = Entry(root, width=35, borderwidth=5, bg="grey", fg="white")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)
    print("Cleared the calculator")


def add():
    first_number = e.get()
    global F_NUM
    global math
    math = "addition"
    F_NUM = int(first_number)
    e.delete(0, END)


def equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, F_NUM + int(second_number))
    if math == "subtraction":
        e.insert(0, F_NUM - int(second_number))
    if math == "multiplication":
        e.insert(0, F_NUM * int(second_number))
    if math == "division":
        e.insert(0, F_NUM / int(second_number))

def subtract():
    first_number = e.get()
    global F_NUM
    global math
    math = "subtraction"
    F_NUM = int(first_number)
    e.delete(0, END)
    pass

def multiply():
    first_number = e.get()
    global F_NUM
    global math
    math = "multiplication"
    F_NUM = int(first_number)
    e.delete(0, END)
    pass

def divide():
    first_number = e.get()
    global F_NUM
    global math
    math = "division"
    F_NUM = int(first_number)
    e.delete(0, END)
    pass

# Define buttons
button_1 = Button(root, text="1", padx=40, pady=20, bg="grey", fg="white", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, bg="grey", fg="white", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, bg="grey", fg="white", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, bg="grey", fg="white", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, bg="grey", fg="white", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, bg="grey", fg="white", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, bg="grey", fg="white", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, bg="grey", fg="white", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, bg="grey", fg="white", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, bg="grey", fg="white", command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, bg="grey", fg="white", command=add)
button_equal = Button(root, text="=", padx=89, pady=20, bg="grey", fg="white", command=equal)
button_clear = Button(root, text="Clear", padx=80, pady=20, bg="grey", fg="white", command=clear)

button_subtract = Button(root, text="-", padx=41, pady=20, bg="grey", fg="white", command=subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, bg="grey", fg="white", command=multiply)
button_divide = Button(root, text="/", padx=41, pady=20, bg="grey", fg="white", command=divide)
button_quit = Button(root, text="Quit", padx=32, pady=10,bg="grey", fg="white", command=root.quit)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=6, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=4, column=1)
button_divide.grid(row=4, column=2)
button_quit.grid(row=7, column=0,)

root.mainloop()
