from tkinter import *
import tkinter.ttk
from PIL import Image, ImageTk
from Conn import *
import Dashboard

def room(new_win6):

    def submit2():
        room = room_value.get()
        avail = avail_value.get()
        status = status_value.get()
        price = price_value.get()
        bed = bed_value.get()
        cur.execute("insert into room(roomnumber,  availability, cleaning_status, price, bed_type) values(%s,%s,%s,%s,%s)",(room, avail, status, price, bed))
        # q="insert into room(roomnumber, availability, cleaning_status, price, bed_type) values(%s,%s,%s,%s,%s)"
        print(room, avail, status, price, bed)
        # cur.execute(q,v)
        mydb.commit()
        change8(new_win6)

    new_win6.title("Add Room")
    new_win6.geometry("850x370+350+200")
    new_win6.resizable(0, 0)
    new_win6.config(background="WHITE")

    img(new_win6)

    Label(new_win6, text="Room Number : ", borderwidth=1, width=15, relief=RIDGE, bg= "White").place(x=30, y=40)
    Label(new_win6, text="Availability : ", borderwidth=1, width=15, relief=RIDGE, bg= "White").place(x=30, y=90)
    Label(new_win6, text="Cleaning Status : ", borderwidth=1, width=15, relief=RIDGE, bg= "White").place(x=30, y=140)
    Label(new_win6, text="Price : ", borderwidth=1, width=15, relief=RIDGE, bg= "White").place(x=30, y=190)
    Label(new_win6, text="Bed Type : ", borderwidth=1, width=15, relief=RIDGE, bg= "White").place(x=30, y=240)

    room_value = StringVar()
    avail_value = StringVar()
    status_value = StringVar()
    price_value = StringVar()
    bed_value = StringVar()

    room_entry = Entry(new_win6, textvariable=room_value)
    price_entry = Entry(new_win6, textvariable=price_value)

    room_entry.place(x=170, y=40, width=145)
    tkinter.ttk.Combobox(new_win6, textvariable=avail_value, values=['Available','Occupied']).place(x=170, y=90)
    tkinter.ttk.Combobox(new_win6, textvariable=status_value, values=['Clean','Messy']).place(x=170, y=140)
    price_entry.place(x=170, y=190, width=145)
    tkinter.ttk.Combobox(new_win6, textvariable=bed_value, values=['Single','Double']).place(x=170, y=240)

    Button(new_win6, text="SUBMIT", command=submit2, bg="WHITE", relief=RIDGE).place(x=100, y=290)
    Button(new_win6, text="CANCEL", bg="WHITE", relief=RIDGE, command=lambda: change7(new_win6)).place(x=170, y=290)




def change8(new_win6):
    new_win6.destroy()
    new_win4 = Tk()
    Dashboard.Dash(new_win4)

def change7(new_win6):
    new_win6.destroy()
    new_win4 = Tk()
    Dashboard.Dash(new_win4)


def img(self, new_win6=None):
    self.img = Image.open("6.jpg")
    self.photo2 = ImageTk.PhotoImage(self.img)
    label3 = Label(image=self.photo2, height=300, width=450)
    label3.place(x=350, y=30)
    # label3.pack()

def call():
    root = Tk()
    room(root)
    root.mainloop()

# call()
