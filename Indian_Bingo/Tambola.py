import random
import tkinter as tk
win=tk.Tk()
win.title('Tambola')
numberframe=tk.LabelFrame(win,text='',bd=0)
numberframe.grid(row=0,column=1,pady=5,padx=5)
# Labels created
def create_labels():
    for j in range(1,10):
        globals() ["label%s"%j]=tk.Label(numberframe,text=j,fg='white',font=('Heventica',15),relief='groove')
        globals() ["label%s"%j].grid(row=1,column=j,ipadx=23,ipady=5)
    globals() ["label10"]=tk.Label(numberframe,text=10,fg='white',font=('Heventica',15),relief='groove')
    globals() ["label10"].grid(row=1,column=10,ipadx=18,ipady=5)   
    for j in range(11,21):
        globals() ["label%s"%j]=tk.Label(numberframe,text=j,fg='white',font=('Heventica',15),relief='groove')
        globals() ["label%s"%j].grid(row=2,column=j-10,ipadx=18,ipady=5)   
    for j in range(21,31):
        globals() ["label%s"%j]=tk.Label(numberframe,text=j,fg='white',font=('Heventica',15),relief='groove')
        globals() ["label%s"%j].grid(row=3,column=j-20,ipadx=18,ipady=5)   
    for j in range(31,41):
        globals() ["label%s"%j]=tk.Label(numberframe,text=j,fg='white',font=('Heventica',15),relief='groove')
        globals() ["label%s"%j].grid(row=4,column=j-30,ipadx=18,ipady=5)   
    for j in range(41,51):
        globals() ["label%s"%j]=tk.Label(numberframe,text=j,fg='white',font=('Heventica',15),relief='groove')
        globals() ["label%s"%j].grid(row=5,column=j-40,ipadx=18,ipady=5)   
    for j in range(51,61):
        globals() ["label%s"%j]=tk.Label(numberframe,text=j,fg='white',font=('Heventica',15),relief='groove')
        globals() ["label%s"%j].grid(row=6,column=j-50,ipadx=18,ipady=5)   
    for j in range(61,71):
        globals() ["label%s"%j]=tk.Label(numberframe,text=j,fg='white',font=('Heventica',15),relief='groove')
        globals() ["label%s"%j].grid(row=7,column=j-60,ipadx=18,ipady=5)   
    for j in range(71,81):
        globals() ["label%s"%j]=tk.Label(numberframe,text=j,fg='white',font=('Heventica',15),relief='groove')
        globals() ["label%s"%j].grid(row=8,column=j-70,ipadx=18,ipady=5)   
    for j in range(81,91):
        globals() ["label%s"%j]=tk.Label(numberframe,text=j,fg='white',font=('Heventica',15),relief='groove')
        globals() ["label%s"%j].grid(row=9,column=j-80,ipadx=18,ipady=5)   
create_labels()

remaining_numbers=[i for i in range(1,91)]
done_numbers=[]

def quit():
    win.destroy()
def click():
    x=random.choice(remaining_numbers)
    # done_numbers.append(x)
    # done_numbers.sort()
    remaining_numbers.remove(x)
    # print(done_numbers)
    globals() ["label%s"%x].config(bg='dodgerblue')
    currentnumberlabeldynamic.config(text=x)
    if remaining_numbers==[]:
        currentnumberlabel.destroy()
        currentnumberlabeldynamic.destroy()
        click_button.destroy()
        quitbutton=tk.Button(outputnumberframe,text='Quit',command=quit,fg='white',bg='dodgerblue',
        font=('Cascadia code',18),activebackground='dodgerblue')
        quitbutton.grid(row=0,column=1,pady=5)
        gameoverlabel=tk.Label(outputnumberframe,text='Game Over!',fg='red',font=('Cascadia Code',30))
        gameoverlabel.grid(row=0,column=0)

outputnumberframe=tk.Frame(win)
outputnumberframe.grid(row=1,column=1)
click_button=tk.Button(outputnumberframe,command=click,text='Roll',font=('Cascadia code',15),bg='dodgerblue',fg='white',activebackground='dodgerblue',activeforeground='white')
click_button.grid(row=0,column=0,padx=5,pady=5)

currentnumberlabel=tk.Label(outputnumberframe,text='Current Number:',fg='black',font=('Cascadia code',18))
currentnumberlabel.grid(row=0,column=1)
currentnumberlabeldynamic=tk.Label(outputnumberframe,bg='dodgerblue',fg='white',font=('Cascadia code',18),relief='groove')
currentnumberlabeldynamic.grid(row=0,column=2,ipadx=8,ipady=3)

win.mainloop()
