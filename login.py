from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox
def signup_page():
    login_window.destroy()
    import signup
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=hide)

#FUNCTIONALITY PART
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def email_enter(event):
    if emailEntry.get()=='email':
        emailEntry.delete(0,END)              
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
        

def login_user():
    Username = usernameEntry.get()
    email = emailEntry.get()
    Password = passwordEntry.get()
    conn = sqlite3.connect("signup.db")
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT PASSWORD FROM signup WHERE username = (?) AND email = (?)',(Username,email))
        pwd_db = cursor.fetchone()[0]
        if pwd_db == Password:
            login_window.destroy() 
            import mainpage
        else:
            messagebox.showerror('Invalid Password','Enter correct password')
    except:
        messagebox.showerror('Invalid details','No such user exists')
    cursor.close()       
    conn.close()  
#GUI PART
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('LOGIN')

login_window.iconphoto(False, ImageTk.PhotoImage(file='logo.png'))
bgImage=ImageTk.PhotoImage(file='bg.jpg')



bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

emailEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
emailEntry.place(x=580,y=260)
emailEntry.insert(0,'Email')
emailEntry.bind('<FocusIn>',email_enter)

frame3 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame3.place(x=580,y=342)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=320)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)

frame2 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=315)

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1')
forgetButton.place(x=720,y=350)

loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=382)


signupLabel=Label(login_window,text="Dont have an account?",font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)

    
login_window.mainloop()