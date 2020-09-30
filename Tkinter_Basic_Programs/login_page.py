from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to Login Page")
window.geometry('250x200+220+220')

l = Label(window, text="Provide Your Credentials").pack()
l1 = Label(window, text="Login ID:-").pack(anchor=W)
e1 = Entry(window,text=StringVar())
e1.pack()
L2 = Label(window, text="Password").pack(anchor=W)
e2 = Entry(window,show= '*',text=StringVar())
e2.pack()

def check():
    a=e1.get()
    b=e2.get()
    if(a=='admin') and (b=='admin'):
        messagebox.showinfo("Welcome page","Your Login ID & Password is correct.")
    else:
        messagebox.showinfo("Keep Trying")
b1 = Button(window, text="Login", command=check).pack()
window.mainloop()
