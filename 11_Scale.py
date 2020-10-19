from tkinter import *

root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='')

def get_price(price_):
    labl_res.config(text=str(price_))
    print(price.get())

price=Scale(root ,from_=2020,to=2024,orient=HORIZONTAL,sliderlength=60,length=300,showvalue=FALSE,command=get_price)
price.place(x=30,y=30)
labl_res=Label(root,fg='black',bg='white')
labl_res.place(x=30,y=70,relwidth=1)
root.mainloop()