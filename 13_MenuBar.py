from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Window')
root.geometry('400x600+700+80')
root.resizable(width=False,height=False)
root.config(bg='')

def employeeDetails():
    messagebox.showinfo( 'showInfo','This is employee details')
MyMenu=Menu(root)
MyMenu.add_command(label='Employee',command=employeeDetails)

# multi DROPDOWN
ViewsMenu=Menu(MyMenu,tearoff=0)
ViewsMenu.add_command(label='View1')
ViewsMenu.add_command(label='View2')
# DROPDOWN
EmployeeInsideMenu=Menu(MyMenu,tearoff=0)
EmployeeInsideMenu.add_command(label='ADD Employee',command=employeeDetails)
EmployeeInsideMenu.add_command(label='Delete Employee',command=employeeDetails)
EmployeeInsideMenu.add_cascade(label='View Employee',menu=ViewsMenu,command=employeeDetails)
EmployeeInsideMenu.add_separator()
EmployeeInsideMenu.add_command(label='EXIT',command=employeeDetails)
# MAIN DROPDOWN
MyMenu.add_cascade(label='Details',menu=EmployeeInsideMenu )

root.config(menu=MyMenu)
root.mainloop()