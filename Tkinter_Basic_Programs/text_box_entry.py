from tkinter import *
window = Tk()  # root window

window.title("Text Box Entry")  # name of the window
l=Label(window,text="Write Anything Here").pack()

e=Entry(window).pack()  #making empty entry box
b=Button(window,text="enter").pack()   #making a button with name enter.

window.mainloop()
