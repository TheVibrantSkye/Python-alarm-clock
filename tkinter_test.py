from tkinter import * # noqa

root = Tk() # noqa


def my_click():
    myLabel = Label(root, text="Look! I clicked a button!").grid(row=3, column=0) # noqa
    print("Called the label after the user clicked the button! woo!")

myButton = Button(root, text="Clicky!", padx=50, command=my_click).grid(row=2, column=0) # noqa

# Creating a Label Widget
myLabel1 = Label(root, text="Hello world!").grid(row=0, column=0) # noqa
myLabel2 = Label(root, text="I'm Skye!").grid(row=1, column=5) # noqa
# Shoving it onto the screen
# myLabel1.grid(row=0,column=0)
# myLabel2.grid(row=1, column=5)


root.mainloop()
