from tkinter import *

root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='#000000')
# Function call when login
def get_name():
    print(username.get())
    print(passwordvar.get())

    login_result.config(text='Successfully Login '+str(username.get()))
# DEFINE MSG VARIBALE
passwordvar=StringVar()
# WELCOME TEXT
lbl1=Label(root,text="Welcome",font=('times new roman',30,'bold'),bg='white',fg='Blue').pack(fill=X)
# LOGIN TEXT
lbl1=Label(root,text="LOGIN",font=('times new roman',20,'bold'),bg='black',fg='yellow').pack(fill=X,pady=10,padx=80)
# INPUT  FEILDS
username=Entry(root,font=('times new roman',10,'bold'),bg='white',fg='black')
username.pack(fill=X ,pady=10,padx=40)

password=Entry(root,font=('times new roman',10,'bold'),textvariable=passwordvar,bg='white',fg='black').place(x=40,y=140,relwidth=0.8)

textmsg=Text(root,font=('times new roman',10,'bold'),bg='white',fg='black',).place(x=40,y=162,relwidth=0.65,width=60,height=60)

# LOGIN BUTTON
btn_get_username=Button(root,text="login",font=('times new roman',15,'bold'),bg='yellow',fg='black',activebackground='green',activeforeground='white',cursor='hand2',command=get_name,padx=5,pady=5).place(x=100,y=240,relwidth=0.5)

# SUCCESS GESTURE
login_result=Label(root,text="",font=('times new roman',10,'bold'),bg='black',fg='green')
login_result.place(x=0,y=280,relwidth=1)
root.mainloop()