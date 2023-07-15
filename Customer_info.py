# import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector
from tkinter import *
import Conn
import Reception

def info(new_win47):
    new_win47.title("Customer Info")
    new_win47.geometry("979x500+300+120")
    new_win47.configure(background="WHITE")
    cols = ('Document', 'Phone Number', 'Name', 'Gender', 'Country', 'Room', 'Checkin Time', 'Deposit')
    listBox = ttk.Treeview(new_win47, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, columns=1, columnspan=1)
        listBox.place(x=10, y=20)
        listBox.column("Document", width=120, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Phone Number", width=120, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Name", width=120, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Gender", width=120, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Country", width=120, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Room", width=120, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Checkin Time", width=120, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Deposit", width=120, anchor=CENTER)
        listBox.place(x=10, y=20)

    Conn.cur.execute("select * from Customer")
    rs = Conn.cur.fetchall()
    # print(rs)
    for i, (document, phnumber, name1, gender, country, room, checkintime, deposit) in enumerate(rs, start=1):
        listBox.insert("", "end", values=(document, phnumber, name1, gender, country, room, checkintime, deposit))
        # Conn.mydb.rollback()
        # Conn.mydb.close()

    # Button(root, text="Back", command= lambda :change(root), bg="WHITE", relief=RIDGE).place(x=450, y=290)
    Button(new_win47, text="Back", command =lambda: change_to_recep33(new_win47), bg="WHITE", relief=RIDGE, width=10).place(x=450, y=290)

def change_to_recep33(new_win51):
    new_win51.destroy()
    new_win52 = Tk()
    Reception.Recep(new_win52)

def call():
    root = Tk()
    info(root)
    root.mainloop()

# call()


