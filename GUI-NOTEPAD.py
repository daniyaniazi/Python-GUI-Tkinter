from tkinter import *
from tkinter import filedialog,messagebox
root = Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False, height=False)
root.config(bg='')

var_filename=StringVar()
def openfiles():
    op=filedialog.askopenfile(title='select file',filetypes=(('text file','.txt'),))
    text_area.insert(END,str(''))
    if op!=None:
        text_area.delete('1.0', END)
        # filenamelbl.config(text='Filename :'+str(op.name.split("/")[-1]))
        var_filename.set(op.name)
        root.title(str(op.name.split("/")[-1]))
        for i in op:
            text_area.insert(END,str(i))
        op.close()

def savefiles():
    if var_filename.get()=='':
        saveasfile()
    else:
        op=open(var_filename.get(),'w')
        op.write(text_area.get('1.0', END))
        op.close()
        messagebox.showinfo('Save As', 'File has been saved')

def saveasfile():
    op = filedialog.asksaveasfile(title='Save as', filetypes=(('text file', '.txt'),),defaultextension='.txt')
    if op != None:
        root.title(str(op.name.split("/")[-1]))
        op.write(text_area.get('1.0',END))
        op.close()
        messagebox.showinfo('Save As','File has been saved')

btn1=Button(root,text='Open',command=openfiles).place(x=10,y=0)
btn2=Button(root,text='Save',command=savefiles).place(x=50,y=0)
btn3=Button(root,text='Save as',command=saveasfile).place(x=85,y=0)
# text area
text_area=Text(root,font=('verdana',10))
text_area.place(x=0,y=20,width=400)
# LABLES
# filenamelbl=Label(root,text='filename')
# filenamelbl.place(x=200,y=0)
root.mainloop()
