#we are creating a simpole formula in python 
from tkinter import *
from tkinter import messagebox
class myform:
    def __init__(self):
        self.root=Tk()
        self.root.title("Sudmit")
        self.l1=Label(self.root,text="Lastname",font=("Arial",18))
        self.l1.grid(row=0)
        self.l2=Label(self.root,text="Firstname",font=("Arial",18))
        self.l2.grid(row=1)
        self.l3=Label(self.root,text="Email",font=("Arial",18))
        self.l3.grid(row=2,sticky=W)
        self.l4=Label(self.root,text="code",font=("Arial",18))
        self.l4.grid(row=3,sticky=W)
        self.firstname=Entry(self.root)
        self.firstname.grid(row=0,column=1,columnspan=2)
        self.last_name=Entry(self.root,)
        self.last_name.grid(row=1,column=1,columnspan=2)
        self.email=Entry(self.root)
        self.email.grid(row=2,column=1,columnspan=2)
        self.code=Entry(self.root,show="*") 
        self.code.grid(row=3,column=1,columnspan=2)
        self.show=Button(self.root,text="Submit",font=("Arial",18),command=self.Thanks)
        self.show.grid(row=4,column=1,padx=4)
        self.quit=Button(self.root,text="Quit",font=("Arial",18),command=self.root.quit)
        self.quit.grid(row=4,column=2,padx=4)
        self.root.mainloop()
        #we are creating this function ,so we can show to the user a message 
    def Thanks(self): 
        messagebox.showinfo("DataSudmited","Thank you")
        self.firstname.delete(0,END)
        self.last_name.delete(0,END)
        self.email.delete(0,END)
        self.code.delete(0,END)
        self.firstname.focus_set()
if __name__=="__main__":
    app=myform()
