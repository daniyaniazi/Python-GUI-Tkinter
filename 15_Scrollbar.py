from tkinter import *

root = Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False, height=False)
root.config(bg='')

window1=Frame(root,bd=2,relief=RIDGE)
window1.place(x=50,y=50,height=200,width=200)

verScroll=Scrollbar(window1,orient=VERTICAL)
verScroll.pack(side=RIGHT,fill=Y)

data=Listbox(window1,font=(20),justify=CENTER,yscrollcommand=verScroll.set)
data.pack(expand=Y)
for i in range(0,101):
    data.insert(i,'Data'+str(i))

verScroll.config(command=data.yview)




root.mainloop()