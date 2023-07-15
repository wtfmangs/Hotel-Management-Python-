from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk
import Conn
import Reception
import tkinter.messagebox as tmsg

def upd(new_win56):

    def check():
        cust_no= cust_value.get()
        # print(cust_no)
        Conn.cur.execute("Select room,name, checkintime, deposit from customer where number = %s ", (cust_no,))
        result = Conn.cur.fetchone()
        Label(new_win56, text=result[0], bg="WHITE").place(x=230, y=113)
        Label(new_win56, text=result[1], bg="WHITE").place(x=230, y=170)
        Label(new_win56, text=result[2], bg="WHITE").place(x=230, y=240)
        Label(new_win56, text=result[3], bg="WHITE").place(x=230, y=310)
        Conn.cur.execute("Select price from room where roomnumber = %s", (result[0],))
        result1=Conn.cur.fetchone()
        global dep
        dep = result1[0]
        pending_amount = eval( f"{result1[0]} - {result[3]}")
        Label(new_win56, text=pending_amount, bg="WHITE").place(x=230, y=380)

    new_win56.geometry("900x500+300+120")
    new_win56.title("Update Status")
    new_win56.config(bg="WHITE")

    fontObj = tkFont.Font(size=15)
    Label(new_win56, text="Customer ID  ", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(x=50, y=50)
    Conn.cur.execute("select number from customer")
    rs=Conn.cur.fetchall()
    cust_value = StringVar()
    tkinter.ttk.Combobox(new_win56, textvariable= cust_value, values=rs).place(x=230, y=60)

    Label(new_win56, text="Room Number ", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(x=50, y=110)
    Label(new_win56, text="Room Number ", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(x=50, y=110)

    Label(new_win56, text="Name ", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W,  bg="WHITE").place(x=50, y=170)

    Label(new_win56, text="Checkin Time", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(x=50, y=240)

    Label(new_win56, text="Amount Paid ", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(x=50, y=310)

    Label(new_win56, text="Pending Amount", borderwidth=1, width=15, relief=FLAT, font=fontObj, anchor=W, bg="WHITE").place(x=50, y=380)

    Button(new_win56, text="Check",  bg="WHITE", relief=RIDGE, width=15, command = lambda: check()).place(x=50, y=430)
    Button(new_win56, text="Update",  bg="WHITE", relief=RIDGE, width=15, command = lambda: update(new_win56)).place(x=180, y=430)
    Button(new_win56, text="Back",  bg="WHITE", relief=RIDGE, width=15, command=lambda : change_to_recep2(new_win56)).place(x=310, y=430)

    img(new_win56)

    def update(new_win60):
        new_win60 = Tk()
        new_win60.title("Update Data")
        new_win60.geometry("250x500+50+120")
        new_win60.config(bg="WHITE")
        fontObj = tkFont.Font(size=15)

        Label(new_win60, text="Enter valid data in each field", bg="WHITE").place(x=50, y=20)
        Label(new_win60, text=cust_value.get(), bg="WHITE").place(x=50, y=50)

        r_value = StringVar()
        r_entry = Entry(new_win60, width=25)
        r_entry.place(x=50, y=110)

        n_value = StringVar()
        n_entry = Entry(new_win60, textvariable=n_value, width=25)
        n_entry.place(x=50, y=170)

        Label(new_win60, text = "Check-In time cannot be changed", bg="WHITE").place(x=50, y=240)

        a_value = StringVar()
        a_entry = Entry(new_win60, textvariable=a_value, width=25)
        a_entry.place(x=50, y=310)

        Button(new_win60, text="Update", bg="WHITE", relief=RIDGE, width=15, command=lambda: update1()).place(x=50,
                                                                                                              y=430)

        def update1(): 
            roomno = r_entry.get()
            name = n_entry.get()
            deposit = a_entry.get()
            Conn.cur.execute("Select room from customer where number = %s ", (cust_value.get(),))
            res = Conn.cur.fetchone()
            Conn.cur.execute("Select price from room where roomnumber = %s", (res[0],))
            result1 = Conn.cur.fetchone()
            dep = result1[0]
            pending_amount = eval(f"{dep}-{deposit}")
            Label(new_win60, text=pending_amount, bg="WHITE").place(x=50, y=380)
            Conn.cur.execute("Update customer set room = %s, name = %s, deposit = %s where number = %s", (roomno, name, deposit, cust_value.get()))
            Conn.mydb.commit()
            tmsg.showinfo("", "Data Updated Successfully")

            change_to_recep5(new_win60, new_win56)

        new_win60.mainloop()

def change_to_recep5(new_win60, new_win56):
    new_win60.destroy()
    new_win56.destroy()
    new_win101 = Tk()
    Reception.Recep(new_win101)

def img(self, root=None):
    self.bg = PhotoImage(file="f.png")
    Label(root, image=self.bg, width=450,height=300,).place(x=400, y=60)

def change_to_recep2(new_win56):
    new_win56.destroy()
    new_win58 = Tk()
    Reception.Recep(new_win58)

def call():
    root = Tk()
    upd(root)
    root.mainloop()

# call()