from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *
import Conn
import Reception

def emp(new_win53):
    # root = Tk()
    new_win53.geometry("750x450+300+120")
    new_win53.title("Employee info")
    new_win53.config(background="WHITE")

    cols = ('name', 'age', 'gender', 'job', 'salary', 'phone', 'email')
    listBox = ttk.Treeview(new_win53, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, columns=1, columnspan=1)
        listBox.column("name", width=100, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("age", width=80, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("gender", width=100, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("job", width=90, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("salary", width=100, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("phone", width=110, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("email", width=150, anchor=CENTER)
        listBox.place(x=10, y=20)

    Conn.cur.execute("select * from employee")
    rs = Conn.cur.fetchall()
    # print(rs)

    for i, (name, age, gender, job, salary, phone, email) in enumerate(rs, start=1):
        listBox.insert("", "end", values=(name, age, gender, job, salary, phone, email))
        # Conn.mydb.rollback()
        # Conn.mydb.close()


    Button(new_win53, text="BACK", bg="WHITE", relief=RIDGE, command=lambda : change_to_recep1(new_win53)).place(x=350, y=290)

def change_to_recep1(new_win53):
    new_win53.destroy()
    new_win54 = Tk()
    Reception.Recep(new_win54)

def call():
    root = Tk()
    emp(root)
    root.mainloop()

# call()