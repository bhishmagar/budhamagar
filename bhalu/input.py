import tkinter
def ClickBtn():
    txt = entry.get()

    button["text"] = txt

root = tkinter.Tk()
root.title("テキスト入力")
root.geometry("400x200")

entry = tkinter.Entry(width=20)
entry.place(x=10 ,y=10)

button = tkinter.Button(text="スタート",command=ClickBtn)
button.place(x=20, y=100)

root.mainloop()