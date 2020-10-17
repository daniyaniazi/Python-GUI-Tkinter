from tkinter import *

root=Tk()
root.title('Window')
root.geometry('700x400+0+0')
root.resizable(width=False,height=False)
root.config(bg='#262626')
# GRID SYSTEM
# label1=Label(root,text="Grid System").grid(row=0,column=0)
# label1=Label(root,text="Grid System").grid(row=0,column=1)
# label1=Label(root,text="Grid System").grid(row=1,column=0)
# label1=Label(root,text="Grid System").grid(row=1,column=1)


# Pack SYSTEM --Grid and Pack cant use together (Inside can use)
# label1=Label(root,text="Pack left System").pack(side=LEFT)
# label1=Label(root,text="Pack fill X System").pack(expand=1,fill=BOTH)
# label1=Label(root,text="Pack System").pack()



# PLACE SYSTEM 
label1=Label(root,text="Pack left System").place(x=0,y=0)
label1=Label(root,text="Pack fill X System").place(x=400,y=300)
label1=Label(root,text="Pack System").place(x=100,y=0)
root.mainloop()
