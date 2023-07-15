from tkinter import *
import Dashboard
import AddEmployee
import AddRoom

def adm(new_win3: object) -> object:
    """

    :rtype: object
    """
    new_win3.title("ADMIN")
    new_win3.geometry("400x200+500+250")
    new_win3.resizable(0, 0)
    new_win3.config(background="WHITE")

    img(new_win3)

    Button(new_win3, text="ADD EMPLOYEES", borderwidth=1, relief=RIDGE, width=20, command=lambda : change5(new_win3)).place(x=50,y=30)
    Button(new_win3, text="ADD ROOMS", borderwidth=1, relief=RIDGE, width=20, command=lambda : change9(new_win3)).place(x=50,y=70)
    Button(new_win3, text="QUIT", borderwidth=1, relief=RIDGE, width=20, command=quit).place(x=50,y=110)
    Button(new_win3, text="BACK", borderwidth=1, relief=RIDGE, width=20, command=lambda : change4(new_win3) ).place(x=50, y= 150)



def img(self, new_win2=None):
    self.bg = PhotoImage(file="4.png")
    Label(new_win2, image=self.bg).place(x=250, y=40)
    #Label(new_win2, image=self.bg).pack()

def change4(new_win3):
    new_win3.destroy()
    new_win4=Tk()
    Dashboard.Dash(new_win4)

def change9(new_win3):
    new_win3.destroy()
    new_win6=Tk()
    AddRoom.room(new_win6)

def change5(new_win3):
    new_win3.destroy()
    new_win4=Tk()
    AddEmployee.emp(new_win4)

def call():
    root = Tk()
    adm(root)
    root.mainloop()

# call()

