import tkinter
window = tkinter.Tk()


def read_data():
    a = data.get()
    print(a)
data = tkinter.Entry(width=50)
data.pack()

butt = tkinter.Button(text="play", command=read_data)
butt.pack()

window.mainloop()