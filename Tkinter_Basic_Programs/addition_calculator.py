from tkinter import *

window = Tk()
window.title("Addition Calculator")
window.geometry('250x200+220+220')

l = Label(window, text="Provide Numbers to Add").pack()
l1 = Label(window, text="Input Number 1").pack(anchor=W)
e1 = Entry(window, text=IntVar())
e1.pack()
L2 = Label(window, text="Input Number 2").pack(anchor=W)
e2 = Entry(window, text=IntVar())
e2.pack()


def add():
    a = e1.get()
    b = e2.get()
    sum=int(a)+int(b)
    print(sum)

b1 = Button(window, text="=", command=add).pack()
window.mainloop()
