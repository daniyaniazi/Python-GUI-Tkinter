from tkinter import *
from tkinter import ttk
root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='')

def get_lang():
    cursor=language_list.curselection()
    print(language_list.get(cursor))


language_list=Listbox(root)
language_list .place(x=30,y=30,width=150)
for i in range(0,20):
    language_list.insert(i,'Language'+str(i))

btn=Button(root,text='submit',command=get_lang).place(x=30,y=200)


def get_Mul_lang():
    cursor=Mul_language_list.curselection() #index
    for i in cursor:
        print(Mul_language_list.get(i))
        Mul_language_list.delete(cursor )


Mul_language_list=Listbox(root,justify=CENTER,selectmode=EXTENDED) #MULTIPLE
Mul_language_list .place(x=200,y=30,width=150)
for i in range(0,20):
    Mul_language_list.insert(i,'Language'+str(i))

btn=Button(root,text='submit',command=get_Mul_lang).place(x=200,y=200)

root.mainloop()