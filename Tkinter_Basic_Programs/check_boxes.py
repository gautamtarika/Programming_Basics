from tkinter import *
window = Tk()  # root window
window.title("Check boxes in Tkinter")

# adding label to window
L = Label(window, text="Your Branch").pack()

var1=IntVar()
R1 = Checkbutton(window, text="BCA",variable=var1).pack( anchor = W )
var2=IntVar()
R2 = Checkbutton(window, text="BBA",variable=var2).pack( anchor = W )

def c():
    print("BCA: %d \nBBA: %d" %(var1.get(),var2.get()))

b1=Button(window,text="Okay", command=c).pack( anchor = W)
b2=Button(window,text="Quit",command=quit).pack(anchor = W)


window.mainloop()
