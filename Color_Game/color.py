import tkinter
import random

win=tkinter.Tk()
win.title('Color Game')
win.geometry('400x300')

text=['YELLOW','RED','ORANGE','GREEN','BLUE','PINK','WHITE','BLACK']
color=[i.lower() for i in text]

labeltext=random.choice(text)
labelcolor=random.choice(color)
lab=tkinter.Label(win,font=("times new roman",50),text=labeltext,fg=labelcolor)
lab.pack()

entry=tkinter.Entry(win,width=15,bd=2)
entry.pack(pady=10)

score=0
scorelabel=tkinter.Label(win,text=('Your','Score' ,'is',score),font=('arial',15))
scorelabel.pack()

def click():
    global score, labelcolor, labeltext
    if (entry.get().lower()==labelcolor):
        score+=10
        entry.delete(0,len(entry.get()))
        scorelabel.config(text=('Your','score','is',score))

    else:        
        scorelabel.config(text=('Your','score','is',score))
        entry.delete(0,10)
    labeltext=random.choice(text)
    labelcolor=random.choice(color)
    lab.config(text=labeltext,fg=labelcolor)
# win.bind('<Return>',click)
def endgame():
    but.config(state='disabled',background='silver')
    # but.destroy()
    timeover=tkinter.Label(win,text='Game Over!',font=('cascadia code',30),fg='red')
    timeover.pack()

but=tkinter.Button(win,text="Enter",font=('arial',20),command=click,background='dodgerblue',activeforeground='white',foreground='white',activebackground='dodgerblue')
but.pack(pady=10)
but.after(30000,endgame)
win.mainloop()


