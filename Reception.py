from tkinter import *

from PIL import Image, ImageTk

import Checkout
import Customer_info
import customer
import Dashboard
import Room
import Employee
import Update
import searchroom


def Recep(new_win2):
    new_win2.geometry("1000x550+250+100")
    new_win2.resizable(0, 0)
    new_win2.title("RECEPTION")
    new_win2.config(background="WHITE")

    img(new_win2)

    Button(text="NEW CUSTOMER FORM", bg="BLACK", fg="WHITE", command=lambda : change_to_form(new_win2)).place(x=50, y=40, width=150, height=35)
    Button(text="ROOM", bg="BLACK", fg="WHITE", command=lambda : change_to_room(new_win2)).place(x=50, y=100, width=150, height=35)
    # Button(text="DEPARTMENTS", bg="BLACK", fg="WHITE").place(x=50, y=150, width=150, height=35)
    Button(text="ALL EMPLOYEES", bg="BLACK", fg="WHITE", command=lambda : change_to_emp(new_win2)).place(x=50, y=160, width=150, height=35)
    Button(text="CUSTOMER INFO", bg="BLACK", fg="WHITE", command=lambda : change_to_info(new_win2)).place(x=50, y=220, width=150, height=35)
    # Button(text="MANAGER INFO", bg="BLACK", fg="WHITE").place(x=50, y=300, width=150, height=35)
    Button(text="CHECKOUT", bg="BLACK", fg="WHITE", command=lambda : change_to_checo(new_win2)).place(x=50, y=280, width=150, height=35)
    Button(text="UPDATE STATUS", bg="BLACK", fg="WHITE", command=lambda : change_to_udp(new_win2)).place(x=50, y=340, width=150, height=35)
    Button(text="SEARCH ROOMS", bg="BLACK", fg="WHITE", command=lambda : change_to_sr(new_win2)).place(x=50, y=400, width=150, height=35)
    Button(text="LOGOUT", bg="BLACK", fg="WHITE", command=lambda : change3(new_win2)).place(x=50, y=460, width=150, height=35)

def img(self, new_win2=NONE):
    self.image = Image.open("DESK.jpg")
    self.photo2 = ImageTk.PhotoImage(self.image)
    label3 = Label(image=self.photo2, height=450, width=700)
    label3.place(x=250, y=40)

def change3(new_win2):
    new_win2.destroy()
    new_win=Tk()
    Dashboard.Dash(new_win)

def change_to_sr(new_win2):
    new_win2.destroy()
    new_win=Tk()
    searchroom.room(new_win)

def change_to_checo(new_win2):
    new_win2.destroy()
    new_win4567=Tk()
    Checkout.checo(new_win4567)

def change_to_emp(new_win2):
    new_win2.destroy()
    new_win55 = Tk()
    Employee.emp(new_win55)

def change_to_udp(new_win2):
    new_win2.destroy()
    new_win57 = Tk()
    Update.upd(new_win57)

def change_to_room(new_win2):
    new_win2.destroy()
    new_win3454 = Tk()
    Room.room(new_win3454)

def change_to_info(new_win2):
    new_win2.destroy()
    new_win3454 = Tk()
    Customer_info.info(new_win3454)

def change_to_form(new_win2):
    new_win2.destroy()
    new_win3454 = Tk()
    customer.cust(new_win3454)


def call():
    root = Tk()
    Recep(root)
    root.mainloop()

# call()