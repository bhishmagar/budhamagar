import tkinter

root = tkinter.Tk()
root.title("画像を表示")

Canvas = tkinter.Canvas(
    root,
    width=400,
    height=500,
    bg="skyblue"
)
Canvas.pack()
img = tkinter.PhotoImage(
    file="panda/h.jpg"
)
Canvas.create_image(200,200, image=img)
root.mainloop()