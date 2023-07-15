import datetime
import tkinter.font as tkFont
from tkinter import *
import tkinter.ttk
import Conn
import Reception
import tkinter.messagebox as tmsg


def checo(root):
    root.geometry("950x500+300+120")
    root.config(bg="WHITE")

    def check():
        cust_no = cust_value.get()

        Conn.cur.execute("Select name,room, checkintime from customer where number = %s ", (cust_no,))
        result = Conn.cur.fetchone()
        Label(root, text=result[0], bg="WHITE", width=15, anchor=W).place(x=230, y=140)
        Label(root, text=result[1], bg="WHITE", width=15, anchor=W).place(x=230, y=210)
        Label(root, text=result[2], bg="WHITE", width=15, anchor=W).place(x=230, y=280)
        ch_value = datetime.datetime.now()
        Label(root, text=f"{ch_value}", background="WHITE").place(x=230, y=340)


    def checkout():
        cust_no = cust_value.get()
        name_gg = name.get()
        Conn.cur.execute("Select room from customer where number = %s ", (cust_no,))
        rn = Conn.cur.fetchone()
        Conn.cur.execute("delete from customer where number= %s", (cust_no,))
        Conn.cur.execute("update room set availability = 'Available' where roomnumber = %s ",(rn))
        Conn.mydb.commit()
        tmsg.showinfo("Success", "Customer Checked Out Successfully")
        change123456(root)

    fontObj = tkFont.Font(size=15)
    name = StringVar()
    Label(root, text="Customer ID ",textvariable=name, borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(
        x=30, y=80)
    Conn.cur.execute("select number from customer")
    rs = Conn.cur.fetchall()
    cust_value = StringVar()
    tkinter.ttk.Combobox(root, textvariable=cust_value, values=rs, width=25).place(x=230, y=80)

    Label(root, text="Name ", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(x=30,
                                                                                                              y=140)

    Label(root, text="Room Number ", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(
        x=30, y=210)

    Label(root, text="Checkin Time ", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(
        x=30, y=280)

    Label(root, text="Checkout Time ", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(
        x=30, y=340)

    def img(self, root=None):
        self.bg = PhotoImage(file="8.PNG")
        Label(root, image=self.bg, width=550).place(x=420, y=20)

    img(self=root)

    Button(root, text="Checkout", command=lambda: checkout(), bg="WHITE", relief=RIDGE, width=15).place(x=150, y=400)
    Button(root, text="Back", command=lambda: change123456(root), bg="WHITE", relief=RIDGE, width=15).place(x=20, y=400)
    Button(root, text="Check", command=lambda: check(), bg="WHITE", relief=RIDGE, width=15).place(x=280, y=400)

def change123456(root):
    root.destroy()
    new_win3454 = Tk()
    Reception.Recep(new_win3454)

def call():
    root = Tk()
    checo(root)
    root.mainloop()

# call()