import tkinter

from panda.bhalu.input import ClickBtn

def Clickbtn():
    button["text"] = "クリックしました！"
root = tkinter.Tk()

root.title("ボタンを作ります")
root.geometry("600x800")

button = tkinter.Button(root,text="ボタンです",
font=("Times New Roman",24),command=ClickBtn)
button.place(x=200,y=200)

root.mainloop()