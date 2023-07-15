from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import ttk
import Reception
import Conn


def room(new_win51):
    new_win51.title("Search Room")
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


    def search_now():


        selected = drop.get()
        if selected == "Search By ...":
           # sql = "SELECT * FROM room WHERE bed_type = %s"
           tmsg.showinfo("Error", "Please select first")
            # test = Label(new_win51, text = "hey! You forget to select the option")
            # test.grid(row=0, columns=2, padx=0,pady=220)

        if selected == "Availability":
            sql = "SELECT * FROM room WHERE availability = %s"
        if selected == "Cleaning Status":
            sql = "SELECT * FROM room WHERE cleaning_status = %s"
        if selected == "Bed Type":
            sql = "SELECT * FROM room WHERE bed_type = %s"
        if selected == "Price":
            sql = "SELECT * FROM room WHERE price = %s"
        if selected == "Room Number":
            sql = "SELECT * FROM room WHERE price = %s"

        searched = search_box.get()
        # sql = "SELECT * FROM room WHERE bed_type = %s"
        name = (searched,)

        result = Conn.cur.execute(sql, name)
        result = Conn.cur.fetchall()
        for i, (roomnumber, availability, cleaning_status, price, bed_type) in enumerate(result, start=1):
            listBox.insert("", "end", values=(roomnumber, availability, cleaning_status, price, bed_type))

        seached_label = Label(new_win51, text=result)
        seached_label.grid(row=2, column=0, padx=10)


    Button(new_win51, text="Back", bg="WHITE", relief=RIDGE, command=lambda : change3456(new_win51)).place(x=400, y=420)
    Button(new_win51, text="Show Selections",bg="WHITE", relief=RIDGE, command=lambda:search_now()).place(x=450, y=420)

    search_box = Entry(new_win51)
    Label(new_win51, text="Search : ", borderwidth=1, width=15, relief=SUNKEN).place(x=50, y=290)
    search_box.grid(row=0, columns=1, padx=170,pady=290)

    drop = ttk.Combobox(new_win51, values= ["Search By ...", "Availability", "Cleaning Status", "Bed Type","Price","Room Number"])
    drop.current(0)
    drop.grid(row=0,column=1 ,padx=90,pady=290 )

def change3456(root):
    root.destroy()
    new_win3454 = Tk()
    Reception.Recep(new_win3454)

def call():
    root = Tk()
    room(root)
    root.mainloop()

# call()