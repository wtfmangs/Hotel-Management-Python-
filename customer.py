import tkinter.ttk
from datetime import datetime
from tkinter import *
import Reception
import Conn

def cust(new_win10):

    def ADD():
        document = document_value.get()
        number = n_value.get()
        name1 = name_value.get()
        gender = g_value.get()
        country = c_value.get()
        room = rn_value.get()
        checkintime = ch_value
        deposit = d_value.get()


        Conn.cur.execute("Insert into Customer(document,number,name,gender,country,room,checkintime,deposit) values(%s,%s,%s,%s,%s,%s,%s,%s)",(document,number,name1,gender,country,room,f"{checkintime}",deposit))
        # q = "insert into employee(name,age,gender,job,salary,phone,email) values(%s,%s,%s,%s,%s,%s,%s)"
        # v = (name,age,gender,job,salary,phone,email1)
        # Conn.mydb.commit()
        Conn.cur.execute("update room set availability = 'Occupied' where roomnumber = %s ",(room ,))
        Conn.mydb.commit()
        change_to_recep78(new_win10)


    new_win10.title("New Customer Form")
    new_win10.geometry("850x470+300+120")
    new_win10.resizable(0, 0)
    new_win10.config(background="WHITE")

    Label(new_win10, text="Document : ", borderwidth=1, width=15, relief=SUNKEN,background="WHITE").place(x=30, y=20)
    Label(new_win10, text="Customer ID : ", borderwidth=1, width=15, relief=SUNKEN,background="WHITE").place(x=30, y=70)
    Label(new_win10, text="Name : ", borderwidth=1, width=15, relief=SUNKEN,background="WHITE").place(x=30, y=120)
    Label(new_win10, text="Gender : ", borderwidth=1, width=15, relief=SUNKEN,background="WHITE").place(x=30, y=170)
    Label(new_win10, text="Country : ", borderwidth=1, width=15, relief=SUNKEN,background="WHITE").place(x=30, y=220)
    Label(new_win10, text="Room Number : ", borderwidth=1, width=15, relief=SUNKEN,background="WHITE").place(x=30, y=270)
    Label(new_win10, text="Checkin Time : ", borderwidth=1, width=15, relief=SUNKEN,background="WHITE").place(x=30, y=320)
    Label(new_win10, text="Deposit : ", borderwidth=1, width=15, relief=SUNKEN,background="WHITE").place(x=30, y=370)

    document_value = StringVar()
    tkinter.ttk.Combobox(new_win10, textvariable=document_value,values=['Passport', 'Driving license', 'Voter-Id Card', 'Ration Card']).place(x=170, y=20)

    n_value = StringVar()
    n_entry = Entry(new_win10, textvariable=n_value)
    n_entry.place(x=170, y=70)

    name_value = StringVar()
    name_entry = Entry(new_win10, textvariable=name_value)
    name_entry.place(x=170, y=120)

    g_value = StringVar()
    Radiobutton(new_win10, text="MALE", padx=14, variable=g_value, value="Male", bg="WHITE").place(x=150, y=170)
    Radiobutton(new_win10, text="FEMALE", padx=14, variable=g_value, value="Female", bg="WHITE").place(x=220, y=170)

    c_value = StringVar()
    c_entry = Entry(new_win10, textvariable=c_value)
    c_entry.place(x=170, y=220)

    Conn.cur.execute("select roomnumber from room where availability='Available'")
    rs=Conn.cur.fetchall()


    rn_value = StringVar()
    tkinter.ttk.Combobox(new_win10, textvariable=rn_value,values=rs,width=20).place(x=170, y=270)

    d_value = StringVar()
    d_entry = Entry(new_win10, textvariable=d_value)
    d_entry.place(x=170, y=370)

    Button(new_win10, text="ADD", bg="WHITE", relief=RIDGE,command =lambda : ADD()).place(x=100, y=420)
    Button(new_win10, text="BACK", bg="WHITE", relief=RIDGE, command=lambda  :change_to_recep78(new_win10)).place(x=170, y=420)

    ch_value = datetime.now()
    Label(new_win10,text=f"{ch_value}",background="WHITE").place(x=170,y=320)

    img(new_win10)

def img(self, new_win10=None):
    self.bg = PhotoImage(file="cus.png")
    Label(new_win10, image=self.bg, width=506 , height=300).place(x=350, y=55)

def change_to_recep78(new_win56):
    new_win56.destroy()
    new_win58 = Tk()
    Reception.Recep(new_win58)

def call():
    root = Tk()
    cust(root)
    root.mainloop()

# call()