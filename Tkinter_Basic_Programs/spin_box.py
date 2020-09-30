from tkinter import *
window = Tk()  # root window
window.title("Spinbox in Tkinter")
s=Spinbox(window,from_=0,to=1000,fg='Green',bg='Cyan').pack()

window.mainloop()
