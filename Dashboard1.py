from tkinter import *
from PIL import Image, ImageTk

import Reception


def Dash2(new_win):

    new_win.title("Dashboard")
    new_win.geometry("1550x1000+0+0")
    new_win.state("zoomed")
    new_win.config(background="WHITE")

    img(new_win)

    Label(text="", background="WHITE").place(x=0, y=0, height=30, width=3200)

    Button(new_win, text="RECEPTION", background="WHITE", borderwidth=0, command=lambda : change1(new_win)).place(x=10, y=5, width=70)
    # Button(new_win, text="ADMIN", background="WHITE", borderwidth=0, command=lambda : change2(new_win)).place(x=80, y=5, width=50)
    Button(new_win, text="QUIT", background="WHITE", borderwidth=0, command=quit).place(x=80, y=5, width=50)

def img(self, new_win=None):
    self.img = Image.open("2.jpg")
    self.photo2 = ImageTk.PhotoImage(self.img)
    label3 = Label(image=self.photo2)
    label3.place()
    label3.pack()

def change1(new_win):
    new_win.destroy()
    new_win1=Tk()
    Reception.Recep(new_win1)

def call():
    root = Tk()
    Dash2(root)
    root.mainloop()

# call()

