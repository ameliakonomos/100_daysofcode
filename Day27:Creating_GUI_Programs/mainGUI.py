#GUI programs, Graphical User Interface
#introduction to Tkinter
import tkinter
from tkinter import *

#buttons class
def button_clicked():
    #prints into the console
    print("I got clicked")
    #reacts when button is clicked
    new_text = input.get()
    my_label.config(text=new_text)

#tkinter creates a window
window = tkinter.Tk() #initialize object from class
window.title("Amelia's GUI Program")
window.minsize(width = 1000, height = 1000)

#Label
my_label = tkinter.Label(text="My First label", font = ("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack(side ="left") #packs a label in program
my_label.place(x=100, y=200)


#Button
button = Button(text = "Click Me", command=button_clicked)
button.pack(side="left")

#Entry Class component
input = Entry()
input.pack(side="left")











#loop keeps window on screen, end of program
window.mainloop()
