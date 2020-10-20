from tkinter import *
from tkinter import filedialog
root = Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False, height=False)
root.config(bg='')

def openfiles():
    # ASK DIRECTORY
    #op=filedialog.askdirectory(title='select folder')
    #op = filedialog.askopenfile(title='select file')

    # op = filedialog.askopenfilename(title='select folder')
    # op = filedialog.askopenfilenames(title='select Multiple files')

    # OBJECT OF FILES
    # op = filedialog.askopenfiles(title='select Multiple files')

    # SAVE FILE --> return obj
    # op = filedialog.asksaveasfile(title='select Multiple files',filetypes=(('text file','.txt'),('all files','*.*')))
    # SAVE FILE --> return filename
    op = filedialog.asksaveasfilename(title='select Multiple files',filetypes=(('text file','.txt'),('all files','*.*')))

    print(op)
    # print(op.split('/')[-1])
    # print(op.name)

btn=Button(root,text='Dialog Box',command=openfiles).place(x=10,y=50)

root.mainloop()