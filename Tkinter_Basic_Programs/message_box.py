from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Welcome Message box")
window.geometry('250x200+200+200')
def hello():
    messagebox.showinfo("Say Hello message box", "Hello! How are you?")

b1=Button(window,text="Press this Button",command=hello).pack()
window.mainloop()