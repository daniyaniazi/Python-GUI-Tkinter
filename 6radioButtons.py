from tkinter import *

root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='')

def getGender():
    print(gender.get())
gender=Label(root,text="SELECT GENDER",font=('times new roman',15,'bold'),bg='gray24',fg='khaki').place(x=10,y=10)

gender=StringVar()
male=Radiobutton(root,text='Male',value='male',variable=gender,font=('times new roman',10,'bold')).place(x=100,y=50)
female=Radiobutton(root,text='Female',value='female',variable=gender,font=('times new roman',10,'bold')).place(x=100,y=80)

gender.set('male')

btn=Button(root,text="show",font=('times new roman',10,'bold'),bg='yellow',fg='black',activebackground='green',activeforeground='white',cursor='hand2',command=getGender).place(x=100,y=120,relwidth=0.15)

root.mainloop()