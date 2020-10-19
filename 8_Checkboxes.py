from tkinter import *

root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='')

def getData():
    print(check_var.get())


check_var=IntVar()
check_box=Checkbutton(root,text='Accept our terms of services',onvalue=1,offvalue=0,variable=check_var,font=('times new roman',20,'bold')).place(x=20,y=50)

btn=Button(root,text="show",font=('times new roman',10,'bold'),bg='yellow',fg='black',activebackground='green',activeforeground='white',cursor='hand2',command=getData).place(x=100,y=120,relwidth=0.15)


root.mainloop()