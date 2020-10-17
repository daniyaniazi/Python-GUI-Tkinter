from tkinter import *

root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='#262626')

lbl1=Label(root,text="Welcome",font=('times new roman',30,'bold'),bg='white',fg='red').pack(fill=X)

lbl1=Label(root,text="LOGIN",font=('times new roman',20,'bold'),bg='black',fg='yellow').pack(fill=X,pady=10,padx=80)

entry1=Entry(root,font=('times new roman',10,'bold'),bg='white',fg='black').pack(fill=X ,pady=10,padx=40)

entry2=Entry(root,font=('times new roman',10,'bold'),bg='white',fg='black').place(x=40,y=160,relwidth=0.5)
root.mainloop()