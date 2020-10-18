from tkinter import *

root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='#000000')
# Function call when login
def get_name():
    print(AddressFeild.get("1.0",END))

lbl1=Label(root,text="Welcome",font=('times new roman',30,'bold'),bg='white',fg='Blue').pack(fill=X)

# name=Entry(root,font=('times new roman',10,'bold'),bg='white',fg='black')
# name.pack(fill=X ,pady=10,padx=40)

AddressFeild=Text(root,font=('times new roman',10,'bold'),bg='white',fg='black',)
AddressFeild.place(x=40,y=162,relwidth=0.65,width=60,height=60)

# LOGIN BUTTON
btn=Button(root,text="login",font=('times new roman',15,'bold'),bg='yellow',fg='black',activebackground='green',activeforeground='white',cursor='hand2',command=get_name,padx=5,pady=5).place(x=100,y=240,relwidth=0.5)

root.mainloop()