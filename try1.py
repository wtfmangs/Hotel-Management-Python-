from tkinter import *
import tkinter.ttk
import tkinter.messagebox as tmsg
import Dashboard
import Dashboard1
from test1 import fun
from PIL import Image, ImageTk
# from Dashboard import *

def log(root):
    def submit():
        user = job_value.get()
        passw = passvalue.get()
        # cur.execute("SELECT * FROM LOGIN")
        # self.rs = cur.fetchone()
        # print(rs)
        if user == "Admin" and passw == "12345":
            # runpy.run_module("tDashboard", init_globals=root)
            # self.new_win = Tk()
            # self.app = Dashboard(self.new_win)
            # root.quit()
            change(root)

        elif user == "Reception" and passw == "12345":
            change_to_dash2(root)

        else:
            tmsg.showinfo("WRONG INPUT", "Invalid Usernane or Password")
            # print("user not found")

    root.title("Login Window")
    root.geometry("400x200+500+250")
    root.resizable(0, 0)
    # root.config(background="Grey")

    f1 = Frame(root, borderwidth=5)

    photo1 = PhotoImage(file="1.png")
    label2 = Label(image=photo1)
    label2.place(x=250, y=30)

    job_value = StringVar()

    Label(f1, text="Username", borderwidth=3).grid(row=0, column=0)
    Label(f1, text="Password").grid(row=1, column=0)

    uservalue = StringVar()
    passvalue = StringVar()

    userentry = Entry(f1, textvariable=uservalue)
    passentry = Entry(f1, textvariable=passvalue, show="*")

    tkinter.ttk.Combobox(f1, textvariable=job_value, values=['Admin', 'Reception'], width=17).grid(row=0, column=1)
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
    Dashboard.Dash(new_win)

def change_to_dash2(root):
    root.destroy()
    new_win=Tk()
    Dashboard1.Dash2(new_win)

def call():
    root = Tk()
    log(root)
    root.mainloop()

call()