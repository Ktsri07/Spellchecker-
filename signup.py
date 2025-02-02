from tkinter import *
from PIL import ImageTk,Image

import sqlite3
import re
from tkinter import messagebox
def login_page():
    signup_window.destroy()
    import login
def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def email_enter(event):
    if emailEntry.get()=='email':
        emailEntry.delete(0,END)              
def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)  
def confirmpassword_enter(event):
    if confirmpasswordEntry.get()=='confirmPassword':
        confirmpasswordEntry.delete(0,END)           
    
def validate_signup(email,Username,Password,confirmPassword):
    def valid_user_name(name):
        pattern =r'^[a-zA-Z0-9._%+-]'
        return bool(re.match(pattern,name))
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    def is_valid_password(password,confirm):
        has_capital_letter = any(char.isupper() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special_symbol = any(char in '!@#$%^&*()_+{}[]:;<>,.?~\\-/' for char in password)
        is_valid_length = 8 <= len(password) <= 20

        if password != confirm:
            messagebox.showerror('Error',"Your password and confirm password doesn't match")
            return False
        elif not (has_capital_letter and has_digit and has_special_symbol and is_valid_length):
            messagebox.showerror("Error", "Password should contain at least a capital letter, digits, and special symbols with a length between 8-20.")
            return False

    if not valid_user_name(Username):
        messagebox.showerror('Invalid User','Enter a valid username')
        return False
    if not is_valid_email(email):
        messagebox.showerror('Invalid Email','Enter a valid email address')
        return False
    if is_valid_password(Password,confirmPassword):
        messagebox.showerror('Invalid ','Passwords does not match')
        return False
    return True

def login_user(email,Username,Password,confirmPassword):
    if validate_signup(email,Username,Password,confirmPassword):
        conn = sqlite3.connect("signup.db")
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS signup (Username TEXT PRIMARY KEY,email TEXT NOT NULL, Password TEXT NOT NULL)')
        cursor.execute('INSERT INTO signup (username, email, password) VALUES (?,?,?)',(Username, email, Password))
        conn.commit()
        messagebox.showinfo("Information","Account created Succesfully! Now you can login")
        conn.close()
    else:
        messagebox.showerror('Invalid signup','Add valid details')


signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')
signup_window.iconphoto(False, ImageTk.PhotoImage(file='logo.png'))

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)
emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmpasswordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

termsandconditions=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',9,'bold'),
                               fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2')
termsandconditions.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',
                    activebackground='firebrick1',activeforeground='white',width=17,command=lambda: login_user(emailEntry.get(), usernameEntry.get(),
                                                 passwordEntry.get(), confirmpasswordEntry.get()))
signupButton.grid(row=10,column=0,pady=10)
alreadyaccount=Label(frame,text="Dont have an account?",font=('Open Sans','9','bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)
loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline')
                   ,bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginButton.place(x=170,y=404)
signup_window.mainloop()