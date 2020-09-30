from tkinter import *

window=Tk()
window.title("Multiplication Table")
EnterTable=IntVar()
l=Label(window,text="Input Any number to find Its Multiplication Table").pack(anchor=W)
e=Entry(window,text=EnterTable)
e.pack(anchor=W)

def MT():
    print("\n")
    for i in range (1,11):
        num=EnterTable.get()
        print(num,'X',i,'=',(i*num))

B=Button(window,text="Calculate",command=MT).pack(anchor=W)
b2=Button(window,text="Quit",command=quit).pack(anchor=W)

window.mainloop()