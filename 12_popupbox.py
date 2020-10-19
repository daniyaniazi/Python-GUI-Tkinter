from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='')

def mesg1():
    messagebox.showerror( 'ShowError','Error msg')
def mesg2():
    messagebox.showinfo( 'showInfo','info msg')
def mesg3():
    messagebox.showwarning( 'ShowWarning','warning msg')




btn1=Button(root,text='mesg1',command=mesg1).place(x=20,y=20)
btn2=Button(root,text='mesg2',command=mesg2).place(x=20,y=60)
btn3=Button(root,text='mesg3',command=mesg3).place(x=20,y=100)


root.mainloop()