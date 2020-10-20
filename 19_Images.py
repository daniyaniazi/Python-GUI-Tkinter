from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False, height=False)
root.config(bg='')


icon=ImageTk.PhotoImage(file='bg.jpg',)
label_img=Label(root,image=icon,).place(x=0,y=0)

# NOT RESIZEBALE
# icon2=PhotoImage(file='login.png',)
# label_img2=Label(root,text='login',padx=10,image=icon2,compound=LEFT).place(x=50,y=50)

#  RESIZEBALE
icon2=Image.open('login.png')
icon2 = icon2.resize((50, 50), Image.ANTIALIAS)
resimg=ImageTk.PhotoImage(icon2)
label_img2=Label(root,text='  Login ',bg='white',font=('times new roman',15,'bold'),image=resimg,compound=LEFT).place(x=160,y=50)

root.mainloop()