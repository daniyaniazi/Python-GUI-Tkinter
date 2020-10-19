from tkinter import *

root = Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False, height=False)
root.config(bg='')

window1=Frame(root)
window1.place(x=5,y=50,height=195,width=200)
btn=Button(window1,text='show').place(x=10,y=50)

window2=LabelFrame(root,text='Student Details',bg='gray34')
window2.place(x=200,y=50,height=195,width=200)
btn2=Button(window2,text='show').place(x=10,y=50)



root.mainloop()