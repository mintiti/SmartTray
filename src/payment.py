from tkinter import *

window = None

def initialize():
    global window
    window = Tk()

    label = Label(fenetre, text="Payment")
    label.pack()

    button=Button(window, text="Fermer", command=window.quit)
    button.pack()

def showWindow():
    global window
    window.mainloop()
    
    
    
    