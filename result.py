from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class result_class:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System ")
        self.root.geometry("1200x700+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #1️⃣1️⃣1️⃣
        title=Label(self.root,text="Add Students Result",compound=LEFT,padx=5,font=("goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,relwidth=1,height=52)
        #Variables=======
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.var_roll=StringVar()
        self.roll_list=[]
        
        self.fetch_roll()
        #===Widgets====

        label_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
        label_name=Label(self.root,text="Name ",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
        label_course=Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=222)
        label_marks_ob=Label(self.root,text="Marks Obtained ",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
        label_full_marks=Label(self.root,text=" Full Marks ",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)

        self.text_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.text_student.place(x=250,y=105,height=30,width=250)
        self.text_student.set("Select")

        button_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        button_search.place(x=510,y=105,width=110,height=30)

        self.text_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20,'bold'),bg="lightyellow",state='readonly')
        self.text_name.place(x=280,y=160,width=335)
        self.text_course=Entry(self.root,textvariable=self.var_course,font=("goudy old style",20,'bold'),bg="lightyellow",state='readonly')
        self.text_course.place(x=280,y=220,width=335)
        self.text_marks=Entry(self.root,textvariable=self.var_marks,font=("goudy old style",20,'bold'),bg="lightyellow")
        self.text_marks.place(x=280,y=280,width=335)
        self.text_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("goudy old style",20,'bold'),bg="lightyellow")
        self.text_full_marks.place(x=280,y=340,width=335)

        #====Button=====
        button_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        button_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)
        #===Image====
        self.bg_image=Image.open("result.jpg")
        self.bg_image=self.bg_image.resize((500,300),Image.ANTIALIAS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)
        self.lbl_image=Label(self.root,image=self.bg_image).place(x=630,y=100)

    #====Function====
    def fetch_roll(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            cur.execute("Select roll From student")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def search(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            cur.execute(f"select name,Course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def add(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search studeents record",parent=self.root)
            
            else:
                cur.execute("Select * From result Where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result is alreay present",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    cur.execute("insert into result(roll,name,course,marks_ob,full_marks,per)values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result added successfully",parent=self.root)
                    
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")
if __name__ == "__main__":
    root = Tk()
    obj = result_class(root)
    root.mainloop()
