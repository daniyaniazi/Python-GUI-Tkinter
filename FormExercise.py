from tkinter import *

root=Tk()
root.title('Registation Form')
root.geometry('400x450+700+80')
root.resizable(width=False,height=False)
root.config(bg='')


def getData():

    username1=username.get()
    password1=password.get()
    gender1=gender.get()
    agree1=check_var.get()
    print(username1,password1,gender1,agree1)
    if agree1==1:
        UserSuccess = Label(root, text="Welcome "+str(username1), font=('Verdana', 15, 'bold'), bg='gray24',fg='khaki').place(x=20,y=380, relwidth=0.95, )
    else:
        UserSuccess = Label(root, text="Please Agree to Our polices", font=('Verdana', 15, 'bold'),bg='gray24', fg='khaki').place(x=20, y=380, relwidth=0.9, )




RehHead=Label(root,text="Registartion Form",font=('Verdana',15,'bold'),bg='gray24',fg='khaki').place(y=5,relwidth=1,)
# BACKGROUND
bg=Label(root,text="",font=('Verdana',15,'bold'),bg='gray24',fg='khaki').place(x=10,y=60,relwidth=0.95,height=400)
# INPUT FEILDS
Labl1=Label(root,text="Enter Username",font=('Verdana',15,'bold'),bg='gray24',fg='white').place(x=20,y=80)
username=Entry(root,font=('Verdana',15,'bold'),bg='white',fg='black')
username.place(x=240,y=80,relwidth=0.3)

Labl2=Label(root,text="Enter password",font=('Verdana',15,'bold'),bg='gray24',fg='white').place(x=20,y=120)
password=Entry(root,font=('Verdana',15,'bold'),bg='white',fg='black')
password.place(x=240,y=120,relwidth=0.3)

# GEBDER
gender=Label(root,text="SELECT GENDER",font=('Verdana',15,'bold'),bg='gray24',fg='white').place(x=20,y=160)

gender=StringVar()
male=Radiobutton(root,text='Male',value='male',variable=gender,font=('Verdana',10,'bold')).place(x=100,y=200)
female=Radiobutton(root,text='Female',value='female',variable=gender,font=('times new roman',10,'bold')).place(x=100,y=240)

gender.set('male')
# AGREE
check_var=IntVar()
check_box=Checkbutton(root,text='Accept our terms of services',onvalue=1,offvalue=0,variable=check_var,font=('Verdana',10,'bold')).place(x=100,y=280)

btn=Button(root,text="show",font=('Verdana',10,'bold'),bg='yellow',fg='black',activebackground='green',activeforeground='white',cursor='hand2',command=getData).place(x=170,y=330,relwidth=0.15)



root.mainloop()