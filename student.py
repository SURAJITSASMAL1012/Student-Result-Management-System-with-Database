from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class Student_Class:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System ")
        self.root.geometry("1200x700+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #1️⃣1️⃣1️⃣
        title=Label(self.root,text="Manage Student Details",compound=LEFT,padx=5,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,relwidth=1,height=40)
        #Variables🤷‍♀️🤷‍♀️
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_dob=StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date=StringVar()
        self.var_state=StringVar()
        self.var_city=StringVar()
        self.var_pin=StringVar()
        #🔢Widgets
        #======Column1=======
        label_roll=Label(self.root,text="Roll No.",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=60)
        label_name=Label(self.root,text="Name ",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=100)
        label_email=Label(self.root,text="Email",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=140)
        label_gender=Label(self.root,text="Gender",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=180)
        label_state=Label(self.root,text="State",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=220)
        label_address=Label(self.root,text="Address",font=("goudy old style",15,'bold'),bg="white").place(x=10,y=260)

        #Entry Fields 
        self.text_roll=Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_roll.place(x=150,y=60)
        self.text_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_name.place(x=150,y=100,width=200)
        self.text_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_email.place(x=150,y=140,width=200)
        self.text_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.text_gender.place(x=150,y=180,width=200)
        self.text_gender.current(0)
        self.text_state=Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_state.place(x=150,y=220,width=200)
        #=====Column 2======
        label_dob=Label(self.root,text="D.O.B ",font=("goudy old style",15,'bold'),bg="white").place(x=365,y=60)
        label_contact=Label(self.root,text="Contact ",font=("goudy old style",15,'bold'),bg="white").place(x=365,y=100)
        label_admission=Label(self.root,text="Admission ",font=("goudy old style",15,'bold'),bg="white").place(x=365,y=140)
        label_course=Label(self.root,text="Course ",font=("goudy old style",15,'bold'),bg="white").place(x=365,y=180)
        label_city=Label(self.root,text="City",font=("goudy old style",15,'bold'),bg="white").place(x=365,y=220)
        label_pin=Label(self.root,text="Pin",font=("goudy old style",15,'bold'),bg="white").place(x=510,y=220)

        #Entry Fields 
        self.course_list=[]
        #Function Call
        self.fetch_course()
        self.text_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_dob.place(x=480,y=60,width=200)
        self.text_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_contact.place(x=480,y=100,width=200)
        self.text_admission=Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_admission.place(x=480,y=140,width=200)
        
        self.text_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",15,'bold'),state='readonly',justify=CENTER)
        self.text_course.place(x=480,y=180,width=200)
        self.text_course.set("Select")
        self.text_city=Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_city.place(x=405,y=220,width=100)
        self.text_pin=Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_pin.place(x=560,y=220,width=100)

        #1️⃣1️⃣Text Field for Addresss1️⃣1️⃣
        
        self.text_address=Text(self.root,font=("goudy old style",15,'bold'),bg="lightyellow")
        self.text_address.place(x=150,y=260,width=535 ,height=100)

        #1️⃣1️⃣1️⃣Button1️⃣1️⃣1️⃣
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
        label_search_roll=Label(self.root,text="Roll ",font=("goudy old style",15,'bold'),bg="white").place(x=720,y=60)
        text_search_roll=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,'bold'),bg="lightyellow").place(x=870,y=60)
        button_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search)
        button_search.place(x=1080,y=60,width=120,height=27)
        #Content
        self.S_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.S_Frame.place(x=720,y=100,width=490,height=340)
        scrolly=Scrollbar(self.S_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.S_Frame,orient=HORIZONTAL)

        self.course_table=ttk.Treeview(self.S_Frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.course_table.xview)
        scrolly.config(command=self.course_table.yview)

        self.course_table.heading("roll",text="Roll No.")
        self.course_table.heading("name",text="Name")
        self.course_table.heading("email",text="Email")
        self.course_table.heading("gender",text="Gender")
        self.course_table.heading("dob",text="D.O.B")
        self.course_table.heading("contact",text="Cotact")
        self.course_table.heading("admission",text="Admission")
        self.course_table.heading("course",text="Course")
        self.course_table.heading("state",text="State")
        self.course_table.heading("city",text="City")
        self.course_table.heading("pin",text="PIN")
        self.course_table.heading("address",text="Address")

        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table["show"]='headings'

        self.course_table.column("roll",width=100)
        self.course_table.column("name",width=120)
        self.course_table.column("email",width=125)
        self.course_table.column("gender",width=125)
        self.course_table.column("dob",width=160)
        self.course_table.column("contact",width=160)
        self.course_table.column("admission",width=160)
        self.course_table.column("course",width=160)
        self.course_table.column("state",width=160)
        self.course_table.column("city",width=160)
        self.course_table.column("pin",width=160)
        self.course_table.column("address",width=160)
        self.course_table.pack(fill=BOTH,expand=1)
        self.course_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_course()
#🔢🔢🔢🔢🔢🔢🔢🔢   
    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set(""),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.var_search.set(""),
        self.text_address.delete("1.0",END),
        #self.text_address(state=NORMAL)
    def delete(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            
            else:
                cur.execute("Select * From student Where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","please select student from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","Do you want to really delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","student deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to  {str(ex)}")
    def get_data(self,ev):
        #self.text_roll.config(state='readonly')
        self.text_roll
        r=self.course_table.focus()
        content=self.course_table.item(r)
        row=content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.text_address.delete("1.0",END),
        self.text_address.insert(END,row[0])
        
    def add(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required",parent=self.root)
            
            else:
                cur.execute("select *  from student Where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll No. is alreay present",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,admission,course,state,city,pin,address)values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.text_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def update(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll no.should be required",parent=self.root)
            
            else:
                cur.execute("Select * From student Where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.text_address.get("1.0",END),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student updated successfully",parent=self.root)
                    self.show()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            cur.execute("Select * From student")
            rows=cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert('',END,values=row)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def fetch_course(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            cur.execute("Select name From course")
            rows=cur.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    def search(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
                self.course_table.delete(*self.course_table.get_children())
                self.course_table.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")



if __name__ == "__main__":
    root = Tk()
    obj = Student_Class(root)
    root.mainloop()
