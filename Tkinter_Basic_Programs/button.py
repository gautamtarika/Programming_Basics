from tkinter import *
window = Tk()  # root window

def act():
    print("Your Name has been recorded")

l=Label(window,text="Write your Name & press enter").pack()
e=Entry(window).pack()
b=Button(window,text="enter",command=act).pack()   #making a button with name enter.

window.mainloop()
