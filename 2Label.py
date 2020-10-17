from tkinter import *

root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='#262626')

lbl1=Label(root,text="Welcome",font=('times new roman',30,'bold'),bg='white',fg='red').pack(fill=X)

lbl2=Label(root,text="User",font=('times new roman',30,'bold'),bg='black',fg='yellow',pady=150,bd=3,relief=RAISED).pack(fill=BOTH,padx=20,pady=5)
# SUNKEN ,GROVE

lbl3=Label(root,text='Good EVE',font=('times new roman',30,'bold'),bg='white',fg='red').place(x=50,y=250,height=100,width=250)

lbl4=Label(root,text="Best Of Luck",font=('times new roman',30,'bold'),bg='white',fg='red').pack(fill=X)
root.mainloop()
