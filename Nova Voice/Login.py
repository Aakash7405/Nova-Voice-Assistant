from tkinter import *
import Main
import pymysql
import messagebox
from PIL import Image,ImageTk

userid=[]
def login():
    if usernameEntry.get() == 'Username' or passEntry.get() == 'Password':
        messagebox.showerror('Error', 'All fields are required')

    else:

        try:
            connection = pymysql.connect(host='localhost', user='root', passwd='@akash#123', port=3306)
            mycursor = connection.cursor()

        except:
            messagebox.showerror('Error', "Database connectivity issue , Please try again")
            return

        query = 'use EchoUserdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passEntry.get()))
        row = mycursor.fetchone()
        userid.append(row[0])
        if row != None:
            messagebox.showinfo('success', 'Login successfully')

            usernameEntry.delete(0, 'end')
            usernameEntry.insert(0, 'Username')
            Echo()



        else:
            messagebox.showerror('Error', "user not exist , please try again")

def Echo():
    root.destroy()
    Main.start()

def hide():
    hide_icon = Button(frame1, image=hideeye, border=0, bg='white', cursor='hand2', command=show)
    hide_icon.place(x=360, y=195)
    passEntry.config(show="*", font=("Brush Script Std", 18))


def show():
    open_icon = Button(frame1, image=openeye, border=0, bg='white', cursor='hand2', command=hide)
    open_icon.place(x=360, y=195)
    passEntry.config(show="", font=('Brush Script Std', 11))


def on_enter(e):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0, 'end')


def on_leave(e):
    name = usernameEntry.get()
    if name == "":
        usernameEntry.insert(0, 'Username')


def on_enter1(e):
   if passEntry.get()=='Password':
    passEntry.delete(0, 'end')


def on_leave1(e):
    passw = passEntry.get()
    if passw == "":
        passEntry.insert(0, 'Password')

def sign_up():
    root.destroy()
    import Registration

root =Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img1 = Image.open("login.jpg")
img1 = img1.resize((470, 490))
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open('avatar.png')
img2 = img2.resize((70, 70))
img2 = ImageTk.PhotoImage(img2)
label1 = Label(root, image=img1)
label1.place(x=0, y=0)

frame1 = Frame(root, width=440, height=450, bg='white')
frame1.place(x=480, y=65)

label3 = Label(frame1, image=img2, bg='white')
label3.place(x=220, y=0)
heading = Label(frame1, text='Welcome', fg='#057B5E', bg='white', font=('Times New Roman', 16, 'bold'))
heading.place(x=212, y=73)

usernameEntry = Entry(frame1, width=25, fg='black', border=0, bg="white", font=('Brush Script Std', 11))
usernameEntry.place(x=100, y=130)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', on_enter)
usernameEntry.bind('<FocusOut>', on_leave)

Frame(frame1, width=295, height=2, bg='black', ).place(x=100, y=155)

passEntry = Entry(frame1, width=25, fg='black', border=0, bg="white", font=('Brush Script Std', 11))
passEntry.place(x=100, y=195)
passEntry.insert(0, 'Password')
passEntry.bind('<FocusIn>', on_enter1)
passEntry.bind('<FocusOut>', on_leave1)

hideeye = Image.open('hideeye.png')
hideeye = hideeye.resize((20, 15))
hideeye = ImageTk.PhotoImage(hideeye)

openeye = Image.open('openeye.png')
openeye = openeye.resize((20, 15))
openeye = ImageTk.PhotoImage(openeye)

show_icon = Button(frame1, image=openeye, border=0, bg='white', cursor='hand2', command=hide)
show_icon.place(x=360, y=195)

Frame(frame1, width=295, height=2, bg='black', ).place(x=100, y=220)

Button(frame1, width=32, pady=7, text='Log in', bg='#049572', fg='white', activebackground='#27B567',
       activeforeground='white', border=0, font=('Times New Roman', 12), command=login).place(x=100, y=260)

label2 = Label(frame1, text="Don't have an account?", fg='black', bg='white', font=('Brush Script Std', 9))
label2.place(x=110, y=320)

sign_up = Button(frame1, width=6, text="Sign Up", border=0, cursor="hand2", fg='#0059FF', bg="white",
                 activeforeground='#0040B1', activebackground='white',command=sign_up)
sign_up.place(x=290, y=317)

root.mainloop()

