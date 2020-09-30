from tkinter import *
window = Tk()  # root window
window.title("Slider in Tkinter")
# making a scroll bar/slider
w=Scale(window, from_=0,to=50,orient=VERTICAL).pack()
#For a vertically oriented slider
w=Scale(window, from_=0,to=50,orient=HORIZONTAL).pack()
#For a horizontally oriented slider

window.mainloop()

