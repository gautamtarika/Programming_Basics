from tkinter import *
from tkinter.ttk import *
window=Tk()
window.title("Combo box Implementation")
l=Label(window,text="Choose your course").pack()
window.geometry('250x200+200+200')
combo=Combobox(window)
combo.pack()
combo['values']=("1","2","3","4","5")
combo.current(0)
window.mainloop()