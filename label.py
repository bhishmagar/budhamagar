from cProfile import label
from cgitb import text
import tkinter
from turtle import color

root = tkinter.Tk()
root.title("初めてのTkinter")
root.geometry("800x600")
label = tkinter.Label(root,text="hey you mother fucker",font=("systeem",30))
label.place(x=200, y=200)
root.mainloop()


