from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class report_class:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System ")
        self.root.geometry("1200x700+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #1️⃣1️⃣1️⃣
        title=Label(self.root,text="View Students Result",compound=LEFT,padx=5,font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,relwidth=1,height=52)

        #===Search===
        self.var_search=StringVar()
        self.var_id=""
        label_search=Label(self.root,text="Search By Roll. No. ",font=("goudy old style",20,"bold"),bg="white").place(x=280,y=100)
        text_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20,"bold"),bg="lightyellow").place(x=510,y=100)

        button_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        button_search.place(x=800,y=105,width=110,height=30)
        button_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=self.clear)
        button_clear.place(x=920,y=105,width=110,height=30)
        #======Label======
        label_roll=Label(self.root,text="Roll",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        label_name=Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        label_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        label_marks=Label(self.root,text="MARKS",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        label_full_marks=Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        label_per=Label(self.root,text="Percentage",font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        self.roll=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)
        self.full_marks=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.full_marks.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root,font=("goudy old style",20,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)

        button_delete=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=self.delete)
        button_delete.place(x=500,y=355,width=110,height=30)
    #=======Function======
    def search(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            
            else:
                cur.execute("select *  from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full_marks.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
                
    def clear(self):
        self.var_rid=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")
        self.var_search.set("")
    def delete(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search students result first",parent=self.root)
            
            else:
                cur.execute("Select * From result Where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("delete","Result deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
if __name__ == "__main__":
    root = Tk()
    obj = report_class(root)
    root.mainloop()
