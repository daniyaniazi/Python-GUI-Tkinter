from tkinter import *
from tkinter import messagebox
import wikipedia

class SearchApp:
    def __init__(self, root):
        self.root= root
        self.root.title=("Search App")
        self.root.geometry('1000x700+0+0')
        self.root.config(bg='gray20')
        

        titlelbl=Label(self.root,text='SearchAPP',font=('helvetica',20,'bold',),bg='gray15',fg='azure',pady=10)
        titlelbl.pack(fill=X)

        search_word_lbl=Label(self.root,text='Search Word',font=('helvetica',15,'bold',),fg='azure',bg='gray20',)
        search_word_lbl.place(x=50,y=100,)

        #GET SEARCH WORD
        self.text_input=StringVar()
        text_entry=Entry(self.root,textvariable=self.text_input,font=('helvetica',15,'bold',),fg='azure',bg='gray27')
        text_entry.place(x=250,y=100)

        search_btn=Button(self.root,text='Search Word',font=('helvetica',10,'bold'),command=self.searchWord,fg='azure',bg='DeepSkyBlue3')
        search_btn.place(x=550,y=100)
        clear_btn=Button(self.root,text='Clear',command=self.clear,font=('helvetica',10,'bold',),fg='azure',bg='DeepSkyBlue3')
        clear_btn.place(x=650,y=100)
        enable_btn=Button(self.root,text='Enable Mode',font=('helvetica',10,'bold',),fg='azure',bg='lime green',command=self.enable)
        enable_btn.place(x=750,y=100)
        disable_btn=Button(self.root,text='Disable Mode',font=('helvetica',10,'bold',),fg='azure',bg='red4',command=self.disable)
        disable_btn.place(x=850,y=100)

        frame1=Frame(self.root,bd=2,relief=RIDGE,bg='gray25')
        frame1.place(x=50,y=170,relwidth=0.9,height=500)

        scrolly=Scrollbar(frame1,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill='y')

        self.text_area=Text(frame1,yscrollcommand=scrolly)
        self.text_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.text_area.yview )
        self.mode_lbl=Label(self.root,text='Mode:',font=('helvetica',10,'bold',),fg='yellow',bg='gray20',)
        self.mode_lbl.place(x=50,y=140)
    def enable(self):
        self.text_area.config(state=NORMAL)
        self.mode_lbl.config(text='Mode: Enable')
    def disable(self):
        self.text_area.config(state=DISABLED)
        self.mode_lbl.config(text='Mode: Disable')

    def searchWord(self):
        if self.text_input.get()=="":
            messagebox.showerror('Error','Empty')
        else:
            fetch_data=wikipedia.summary(self.text_input.get())
            self.text_area.insert('1.0',fetch_data)

    def clear(self):
        self.text_input.set(' ')
        self.text_area.delete('1.0',END)
        self.mode_lbl.config(text='Mode:')


root=Tk()
obj=SearchApp(root)
root.mainloop()