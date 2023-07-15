import tkinter
import PIL
from  tkinter import *

def screen2(root):
    root.title("Screen2")
    root.geometry("400x200+500+250")
    Label(root, text="Screen 2").pack()

    img = tkinter.PhotoImage(file="1.png")
    Label(root, image=img).pack()

def fun():
    root = Tk()
    screen2(root)
    root.mainloop()