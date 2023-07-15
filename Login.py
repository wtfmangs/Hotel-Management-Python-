from tkinter import *
import tkinter.messagebox as tmsg
from test1 import fun
from PIL import Image, ImageTk
from Dashboard import *

def log(root):
    def submit():
        user = uservalue.get()
        passw = passvalue.get()
        # cur.execute("SELECT * FROM LOGIN")
        # self.rs = cur.fetchone()
        # print(rs)
        if user == "admin" and passw == "12345":
            sarv = "admin"
            # runpy.run_module("tDashboard", init_globals=root)
            # self.new_win = Tk()
            # self.app = Dashboard(self.new_win)
            # root.quit()
            change(root)

        else:
            tmsg.showinfo("WRONG INPUT", "Invalid Usernane or Password")
            # print("user not found")

    root.title("Login Window")
    root.geometry("400x200+500+250")
    root.resizable(0, 0)
    # root.config(background="WHITE")

    f1 = Frame(root, borderwidth=5)

    photo1 = PhotoImage(file="1.png")
    label2 = Label(image=photo1)
    label2.place(x=250, y=30)

    Label(f1, text="Username", borderwidth=3).grid(row=0, column=0)
    Label(f1, text="Password").grid(row=1, column=0)

    uservalue = StringVar()
    passvalue = StringVar()

    userentry = Entry(f1, textvariable=uservalue)
    passentry = Entry(f1, textvariable=passvalue, show="*")

    userentry.grid(row=0, column=1)
    passentry.grid(row=1, column=1)

    img(root)

    Button(f1, text="SUBMIT", command=submit).grid(row=2, column=0, pady=5)
    Button(f1, text="CLOSE", command=root.destroy).grid(row=2, column=1, pady=5)
    f1.place(x=50, y=50)

def img(self, root=None):
    self.bg = PhotoImage(file="1.png")
    Label(root, image=self.bg).place(x=250, y=30)

def change(root):
    root.destroy()
    new_win=Tk()
    Dash(new_win)

def call():
    root = Tk()
    log(root)
    root.mainloop()

call()