from tkinter import *
from tkinter import ttk
root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='')

def get_data():
    print(language.get())

language=ttk.Combobox(root,values=('php','js','python','java'),state='readonly',justify=CENTER)
language.place(x=30,y=50,width=300) #no bg,fg
# language.current(0)
language.set('Language')
btn=Button(root,text='submit',command=get_data).place(x=30,y=70)
root.mainloop()
