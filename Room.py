from tkinter import *
from tkinter import ttk
import Conn
import Reception

def room(new_win51):
    # new_win51 = Tk()
    new_win51.title("Room")
    new_win51.geometry("935x500+300+120")
    new_win51.config(bg="WHITE")
    cols = ('Room number', 'Availability', 'Cleaning status', 'Price', 'Bedtype')
    listBox = ttk.Treeview(new_win51, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, columns=1, columnspan=1)
        listBox.place(x=10, y=20)
        listBox.column("Room number", width=150, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Availability", width=200, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Cleaning status", width=200, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Price", width=180, anchor=CENTER)
        listBox.place(x=10, y=20)
        listBox.column("Bedtype", width=180, anchor=CENTER)
        listBox.place(x=10, y=20)

    Conn.cur.execute("select * from room")
    rs = Conn.cur.fetchall()
    for i, (roomnumber, availability, cleaning_status, price, bed_type) in enumerate(rs, start=1):
        listBox.insert("", "end", values=(roomnumber, availability, cleaning_status, price, bed_type))
        # Conn.mydb.rollback()
        # Conn.mydb.close()

    Button(new_win51, text="Back", bg="WHITE", relief=RIDGE, command=lambda : change_to_recep(new_win51)).place(x=450, y=290)
    # Button(new_win51, text="filter", bg="WHITE", relief=RIDGE).place(x=350, y=290)

def change_to_recep(new_win51):
    new_win51.destroy()
    new_win52 = Tk()
    Reception.Recep(new_win52)

def call():
    root = Tk()
    room(root)
    root.mainloop()

# call()

