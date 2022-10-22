import random
from pyperclip import copy
import tkinter as tk

win=tk.Tk()
win.title('Password Generator')
labf=tk.LabelFrame(win,text='Controls',font=('times new roman',20),bd=3)
labf.pack(side='bottom',pady=5,padx=5)
lower=list('abcdefghijklmnopqrstuvwxyz')
upper=list(i.upper() for i in lower)
digits=list('1234567890')
symbols=list('!@#$%^&*()_+=?></')
character=lower+upper+digits+symbols

def passwd():
    global password
    password=''
    for _ in range(12):
        password+=random.choice(character)
    passwordlabel.config(text=password)
    
    labtop.pack(padx=5,pady=5)
    passwordlabel.pack(side='left') 
    copytoclipboard.pack(side='bottom',padx=5,pady=5)
    savepasswordbutton.pack(ipadx=20,ipady=0,pady=5)
    
generatepasswordbutton=tk.Button(labf,bg='dodgerblue',fg='white',text="Generate Password",activeforeground='white',
            activebackground='dodgerblue',command=passwd,font=('heventica',20,'italic'))
generatepasswordbutton.pack(side='bottom',padx=5,pady=5)
labtop=tk.LabelFrame(win,bd=3,text="Your Password is . . .",font=('times new roman',20))
passwordlabel=tk.Label(labtop,text='',font=('heventica',20),fg='mediumvioletred')

def copy1():
    copy(password)

copytoclipboard=tk.Button(labf,bg='dodgerblue',activebackground='dodgerblue',activeforeground='white',
            fg='white',text="Copy To ClipBoard",command=copy1,font=('heventica',20,'italic'))

def save():
    root=tk.Tk()
    root.geometry('250x130')
    usernamewidget=tk.Entry(root,width=30,bd=3)
    usernamewidget.pack(pady=5,padx=5)
    usernamewidget.insert(0,"Enter Username for Password :")
    usernamewidget.focus_set()
    websitenamewidget=tk.Entry(root,width=30,bd=3)
    websitenamewidget.pack(pady=5,padx=5)
    websitenamewidget.insert(0,"Enter Website for Password :")
    root.title("Save Password")

    def savepwd():
        file=open("password.txt",'a')
        file.write(f'Username : {usernamewidget.get()}\nWebsite : {websitenamewidget.get()}\nPassword : {password}\n')
        file.write('-----------------------------------------------------\n')
        file.close()
        root.destroy()
        # savepasswordbutton.config(state='disabled',bg='darkgrey',text="Password Saved")
        
    enterbutton=tk.Button(root,text='Enter',command=savepwd,bg='dodgerblue',activebackground='dodgerblue',
                fg='white',activeforeground='white',font=('heventica',15,'italic'))
    enterbutton.pack(pady=5,padx=5)

savepasswordbutton=tk.Button(labf,text="Save Password",activebackground='dodgerblue',bg='dodgerblue',
            activeforeground='white',fg='white',command=save,font=('heventica',20,'italic'))
            
win.mainloop()
