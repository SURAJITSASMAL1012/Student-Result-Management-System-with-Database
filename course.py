from tkinter import*
from turtle import up, update
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class Course_Class:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System ")
        self.root.geometry("1200x700+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #1️⃣1️⃣1️⃣
        title=Label(self.root,text="Manage Course Details",compound=LEFT,padx=5,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,relwidth=1,height=40)
        #Variables🤷‍♀️🤷‍♀️
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()
        #🔢Widgets
        label_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=60)
        label_duration=Label(self.root,text="Duration",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=100)
        label_charges=Label(self.root,text="Charges",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=140)
        label_description=Label(self.root,text="Dsescription",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=180)

        self.text_courseName=Entry(self.root,textvariable=self.var_course,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_courseName.place(x=150,y=60)
        self.text_duration=Entry(self.root,textvariable=self.var_duration,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_duration.place(x=150,y=100,width=200)
        self.text_charges=Entry(self.root,textvariable=self.var_charges,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_charges.place(x=150,y=140,width=200)
        self.text_description=Text(self.root,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_description.place(x=150,y=180,width=500,height=160)

        #Button
        self.button_add=Button(self.root,text='Save',font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.button_add.place(x=150,y=400,width=110,height=40)

        self.button_update=Button(self.root,text='Update',font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.button_update.place(x=270,y=400,width=110,height=40)

        self.button_delete=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.button_delete.place(x=390,y=400,width=110,height=40)

        self.button_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear )
        self.button_clear.place(x=510,y=400,width=110,height=40)
        #search Pannel
        self.var_search=StringVar()
        label_search_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,'bold'),bg="white").place(x=720,y=60)
        text_search_courseName=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg="lightyellow").place(x=870,y=60)
        button_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        button_search.place(x=1080,y=60,width=120,height=27)
        #Content
        self.S_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.S_Frame.place(x=720,y=100,width=490,height=340)
        scrolly=Scrollbar(self.S_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.S_Frame,orient=HORIZONTAL)

        self.course_table=ttk.Treeview(self.S_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)

        self.course_table.heading("cid",text="Course Id")
        self.course_table.heading("name",text="Name")
        self.course_table.heading("duration",text="Duration")
        self.course_table.heading("charges",text="Charges")
        self.course_table.heading("description",text="Description")

        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table["show"]='headings'

        self.course_table.column("cid",width=90)
        self.course_table.column("name",width=150)
        self.course_table.column("duration",width=125)
        self.course_table.column("charges",width=125)
        self.course_table.column("description",width=160)
        self.course_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#🔢🔢🔢🔢🔢🔢🔢🔢   
    def clear(self):
        self.show
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.text_description.delete('1.0',END)
        self.text_courseName.config(state=NORMAL)
    def delete(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            
            else:
                cur.execute("Select * From course Where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","please select course from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you want to really delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","course deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def get_data(self,ev):
        self.text_courseName.config(state='readonly')
        self.text_courseName
        r=self.course_table.focus()
        content=self.course_table.item(r)
        row=content["values"]
        #print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.text_description.delete('1.0',END)
        self.text_description.insert(END,row[4])
    def add(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            
            else:
                cur.execute("Select * From course Where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course name is alreay present",parent=self.root)
                else:
                    cur.execute("insert into course(name,duration,charges,description)values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.text_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def update(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required",parent=self.root)
            
            else:
                cur.execute("Select * From course Where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select Course from list",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where name=?",(
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.text_description.get("1.0",END),
                        #self.text_courseName.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course update d successfully",parent=self.root)
                    self.show()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            cur.execute("Select * From course ")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)


        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def search(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            cur.execute(f"Select * From course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)


        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")



if __name__ == "__main__":
    root = Tk()
    obj = Course_Class(root)
    root.mainloop()
