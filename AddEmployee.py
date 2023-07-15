import tkinter.ttk
from tkinter import *
import Dashboard
from Conn import *
import tkinter.messagebox as tmsg
import PIL

def emp(new_win5):

    def submit1():
        name = name_value.get()
        age = age_value.get()
        gender = gender_value.get()
        job = job_value.get()
        salary = salary_value.get()
        phone = phone_value.get()
        email1 = email_value.get()
        # print(name, age, gender, job, salary, phone, email1)
        # cur.execute(f"insert into employee values({name}, {age}, {gender}, {job}, {salary}, {phone}, {email1})")
        cur.execute("insert into employee(name,age,gender,job,salary,phone,email) values(%s,%s,%s,%s,%s,%s,%s)",(name,age,gender,job,salary,phone,email1))
        # q = "insert into employee(name,age,gender,job,salary,phone,email) values(%s,%s,%s,%s,%s,%s,%s)"
        # v = (name,age,gender,job,salary,phone,email1)
        # cur.execute(q,v)
        mydb.commit()
        changee(new_win5)

    new_win5.title("Add Employee")
    new_win5.geometry("850x470+300+120")
    new_win5.resizable(0, 0)
    new_win5.config(background="WHITE")

    Label(new_win5, text="Name : ", borderwidth=1, width=15, relief=SUNKEN).place(x=30, y=70)
    Label(new_win5, text="Age : ", borderwidth=1, width=15, relief=SUNKEN).place(x=30, y=120)
    Label(new_win5, text="Gender : ", borderwidth=1, width=15, relief=SUNKEN).place(x=30, y=170)
    Label(new_win5, text="Job : ", borderwidth=1, width=15, relief=SUNKEN).place(x=30, y=220)
    Label(new_win5, text="Salary : ", borderwidth=1, width=15, relief=SUNKEN).place(x=30, y=270)
    Label(new_win5, text="Phone : ", borderwidth=1, width=15, relief=SUNKEN).place(x=30, y=320)
    Label(new_win5, text="EMAIL : ", borderwidth=1, width=15, relief=SUNKEN).place(x=30, y=370)

    name_value = StringVar()
    name_entry = Entry(new_win5, textvariable=name_value)
    name_entry.place(x=170, y=70)

    age_value = StringVar()
    age_entry = Entry(new_win5, textvariable=age_value)
    age_entry.place(x=170, y=120)

    gender_value = StringVar()
    Radiobutton(new_win5, text="MALE", padx=14, variable=gender_value, value="Male", bg="WHITE").place(x=150, y=170)
    Radiobutton(new_win5, text="FEMALE", padx=14, variable=gender_value, value="Female", bg="WHITE").place(x=220, y=170)

    job_value = StringVar()
    tkinter.ttk.Combobox(new_win5, textvariable=job_value, values=['Front Desk Clerks','Porters','House Keeping','Kitchen Staff','Waiter','Room Service','Manager'], state="").place(x=170, y=220)

    salary_value = StringVar()
    salary_entry = Entry(new_win5, textvariable=salary_value)
    salary_entry.place(x=170, y=270)

    phone_value = StringVar()
    phone_entry = Entry(new_win5, textvariable=phone_value)
    phone_entry.place(x=170, y=320)

    email_value = StringVar()
    email_entry = Entry(new_win5, textvariable=email_value)
    email_entry.place(x=170, y=370)

    Button(new_win5, text="SUBMIT", command=submit1, bg="WHITE", relief=RIDGE).place(x= 100, y=420)
    Button(new_win5, text="CANCEL", bg="WHITE", relief=RIDGE, command=lambda : change4(new_win5)).place(x= 170, y=420)

    img(new_win5)

def img(self, new_win5=None):
    self.bg = PhotoImage(file="5.png")
    Label(new_win5, image=self.bg, width=450).place(x=350, y=60)

def change4(new_win3):
    new_win3.destroy()
    new_win4=Tk()
    Dashboard.Dash(new_win4)

def changee(new_win3):
    new_win3.destroy()
    new_win4=Tk()
    Dashboard.Dash(new_win4)

def call():
    root = Tk()
    emp(root)
    root.mainloop()

# call()
