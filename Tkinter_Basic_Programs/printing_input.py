#in this program we will be reading theinput that user input in new window and printing that.
from tkinter import *
window = Tk()  # root window

svalue=StringVar()
w=Entry(window,text=svalue).pack()

def act():
    print("Your Name has been recorded")
    print('%s' %svalue.get())

l = Label(window, text="Write your Name & press enter").pack()

# making a button with name enter.
b = Button(window, text="enter", command=act).pack()

window.mainloop()
