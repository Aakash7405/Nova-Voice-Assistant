from tkinter import*
import pymysql
import messagebox
from PIL import Image,ImageTk


def on_enterrepass(e):
  if rePassEntry.get()=='Confirm Password':
    rePassEntry.delete(0, 'end')


def on_leaverepass(e):
    name = rePassEntry.get()
    if name == "":
        rePassEntry.insert(0, 'Confirm Password')


def on_entername(e):
    if usernameEntry.get() =='Enter Name':
        usernameEntry.delete(0, 'end')


def on_leavename(e):
    name = usernameEntry.get()
    if name == "":
        usernameEntry.insert(0, 'Enter Name')


def on_enteremail(e):
    if emailEntry.get() == "Enter Email":
      emailEntry.delete(0, 'end')


def on_leaveemail(e):
    name = emailEntry.get()
    if name == "":
        emailEntry.insert(0, 'Enter Email')


def on_entercontact(e):
   if contactEntry.get()=='Contact No':
    contactEntry.delete(0, 'end')


def on_leavecontact(e):
    name = contactEntry.get()
    if name == "":
        contactEntry.insert(0, 'Contact No')


def on_enterpass(e):
  if passwordEntry.get()=='Password':
    passwordEntry.delete(0, 'end')


def on_leavepass(e):
    name = passwordEntry.get()
    if name == "":
        passwordEntry.insert(0, 'Password')


def clear():
    usernameEntry.delete(0, END)
    usernameEntry.insert(0, 'Enter Name')
    emailEntry.delete(0, END)
    emailEntry.insert(0, 'Enter Email')
    contactEntry.delete(0, END)
    contactEntry.insert(0, 'Contact No')
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, 'Password')
    rePassEntry.delete(0, END)
    rePassEntry.insert(0, 'Confirm Password')

def checkNumber(str):
    for i in str:
        if (i.isdigit()):
            return True

    return False

def checkString(str):
    flag = 0
    for i in str:
        if ((i.isdigit())==False):
            flag=1


    if flag==1:
        return True
    else:
        return False


def connect_database():
    str1=usernameEntry.get()

    if (usernameEntry.get()) == "Enter Name" or emailEntry.get() == "Enter Email" or contactEntry.get() == "Contact No" or passwordEntry.get() == "Password" or rePassEntry.get() == "Confirm Password":
        messagebox.showerror('Error', 'All fields are required')

    elif (checkNumber(str1)):
        messagebox.showerror('Error',"Name field must have only alphabets")

    elif "@gmail.com" not in (emailEntry.get()):
        messagebox.showerror('Error', 'Incorrect Email')

    elif len(contactEntry.get()) != 10:
        messagebox.showerror('Error', 'contact number must have 10 Characters')

    elif (checkString(contactEntry.get())):
        messagebox.showerror('Error', 'contact number must have only digits')

    elif len(passwordEntry.get())<8:
        messagebox.showerror('Error',"password  field contains at least 8 characters")

    elif passwordEntry.get() != rePassEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')

    else:
        try:
            con = pymysql.connect(host="localhost", user="root", passwd="your_pass", port=3306)
            mycursor = con.cursor()

        except:
            messagebox.showerror('Error', 'Database Connectivity Issue , Please Try Again')
            return

        try:
            query = 'create database NovaData'
            mycursor.execute(query)
            query = 'use EchoUserdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use NovaUserData')

        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))
        n = mycursor.fetchone()

        if n != None:
            messagebox.showerror('Error', 'Name already exists')

        else:
            query = 'select * from data where email=%s'
            mycursor.execute(query, (emailEntry.get()))
            mail = mycursor.fetchone()

            if mail != None:
                messagebox.showerror('Error','Email Already exists')
            else:
                query = 'insert into data(email,username,password) values(%s,%s,%s)'
                mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('success', 'Registration is successful')

                login()


def login():
    base.destroy()
    import Login


base=Tk()
base.geometry("925x500+300+200")
base.title("Registration form")
base.configure(bg="#fff")
base.resizable(False, False)

img = Image.open("Mobile-login-Cristina.jpg")
img = img.resize((470, 490))
img = ImageTk.PhotoImage(img)
l = Label(base, image=img)
l.place(x=0, y=0)

fm1 = Frame(base, width=440, height=450, bg='white')
fm1.place(x=480, y=35)

lb = Label(fm1, text="Create New Account", width=25, fg='#057B5E', bg='white', font=("Times New Roman", 23, "bold"))
lb.place(x=0, y=20)

usernameEntry = Entry(fm1, width=30, fg='black', border=0, bg='white', font=('Brush Script Std', 11))
usernameEntry.place(x=40, y=90)
usernameEntry.insert(0, 'Enter Name')
usernameEntry.bind('<FocusIn>', on_entername)
usernameEntry.bind('<FocusOut>', on_leavename)
Frame(fm1, width=330, height=2, bg='black').place(x=40, y=110)

emailEntry = Entry(fm1, width=30, fg='black', border=0, bg='white', font=('Brush Script Std', 11))
emailEntry.place(x=40, y=140)
emailEntry.insert(0, 'Enter Email')
emailEntry.bind('<FocusIn>', on_enteremail)
emailEntry.bind('<FocusOut>', on_leaveemail)
Frame(fm1, width=330, height=2, bg='black').place(x=40, y=160)

contactEntry = Entry(fm1, width=30, fg='black', border=0, bg='white', font=('Brush Script Std', 11))
contactEntry.place(x=40, y=190)
contactEntry.insert(0, 'Contact No')
contactEntry.bind('<FocusIn>', on_entercontact)
contactEntry.bind('<FocusOut>', on_leavecontact)
Frame(fm1, width=330, height=2, bg='black').place(x=40, y=210)

passwordEntry = Entry(fm1, width=30, fg='black', border=0, bg='white', font=('Brush Script Std', 11))
passwordEntry.place(x=40, y=240)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', on_enterpass)
passwordEntry.bind('<FocusOut>', on_leavepass)
Frame(fm1, width=330, height=2, bg='black').place(x=40, y=260)

rePassEntry = Entry(fm1, width=30, fg='black', border=0, bg='white', font=('Brush Script Std', 11))
rePassEntry.place(x=40, y=290)
rePassEntry.insert(0, 'Confirm Password')
rePassEntry.bind('<FocusIn>', on_enterrepass)
rePassEntry.bind('<FocusOut>', on_leaverepass)
Frame(fm1, width=330, height=2, bg='black').place(x=40, y=310)

register = Button(fm1, width=36, pady=7, text='Sign Up', bg='#049572', fg='white', activebackground='#27B567',
                  activeforeground='white', border=0, font=('Times New Roman', 12,'bold'), command=connect_database)
register.place(x=40, y=350)

label=Label(fm1,text="Already have an Account ?",bg='white',fg='black',border=0,font=('Times New Roman', 11))
label.place(x=40,y=405)

Login_Button = Button(fm1, width=6, text="Log In", border=0, cursor="hand2", fg='#0059FF', bg="white",
                      activeforeground='#0040B1', activebackground='white',font=('Times New Roman', 12,'bold'), command=login)
Login_Button.place(x=300, y=400)


base.mainloop()






