from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3#pip install pymysql
import os
class register_class:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1400x750+0+0")
        self.root.config(bg="white")

        #⭐⭐BG Image⭐⭐
        self.bg_img=ImageTk.PhotoImage(file="bg_register.jpg")
        bg_img=Label(self.root,image=self.bg_img).place(x=200,y=0)
        #🐤🐤left Image🐤🐤
        self.left_img=ImageTk.PhotoImage(file="side.png")
        left_img=Label(self.root,image=self.left_img).place(x=80,y=100,width=400,height=500)

        #Register Frame
        register_frame1=Frame(self.root,bg="white")
        register_frame1.place(x=482,y=102,width=701,height=501)
        #Row 1
        
        register_title=Label(register_frame1,text="REGISTER HERE ",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        first_name=Label(register_frame1,text="First Name ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(register_frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=245)
        last_name=Label(register_frame1,text="Last Name ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(register_frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=245)
        #🐤🐤🐤🐤🐤🐤Row2
        contact=Label(register_frame1,text="Contact No ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(register_frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=245)
        email=Label(register_frame1,text="Email ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(register_frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=245)
        #🐤🐤🐤🐤🐤Row3
        question=Label(register_frame1,text="Security Question ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.box_question=ttk.Combobox(register_frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.box_question['values']=("Select","Your Birth Place","Your Best Friend Name","Your Favorite fruit")
        self.box_question.place(x=50,y=270,width=245)
        self.box_question.current(0)
        answer=Label(register_frame1,text="Answer ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(register_frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=245)
        #🐤🐤🐤🐤🐤🐤Row4
        password=Label(register_frame1,text="Password",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(register_frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=245)
        confirmp=Label(register_frame1,text="Confirm Password ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_confirmp=Entry(register_frame1,font=("times new roman",15),bg="lightgray")
        self.txt_confirmp.place(x=370,y=340,width=245)
        #Terms and condition
        self.var_chk=IntVar()
        chck=Checkbutton(register_frame1,text="I Agree The terms & conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12),bg="white").place(x=50,y=380)
        self.button_img=ImageTk.PhotoImage(file="register.png")
        button_register=Button(register_frame1,image=self.button_img,bd=0,cursor="hand2",command=self.reister_data).place(x=50,y=420)
        button=Button(self.root,text="Sign In",font=("times new roman",18),bd=0,cursor="hand2",command=self.login_window).place(x=195,y=460,width=170)
    #def clear(Self):
        #self.txt_fname.delete
    def login_window(self):
        self.root.destroy()
        #import LogIn
        os.system("python LogIn.py")

    def clear(Self):
        Self.txt_fname.delete(0,END)
        Self.txt_lname.delete(0,END)
        Self.txt_contact.delete(0,END)
        Self.txt_email.delete(0,END)
        Self.txt_answer.delete(0,END)
        Self.txt_password.delete(0,END)
        Self.txt_confirmp.delete(0,END)
        Self.box_question.delete(0,END)
    def reister_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.box_question.get()=="Select" or self.txt_answer.get()=="" or  self.txt_password.get()=="" or self.txt_confirmp.get()=="":
            messagebox.showerror("Error","All fields are required ")
        elif self.txt_password.get()!=self.txt_confirmp.get():
            messagebox.showerror("Error","Password & Confirm password ,should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our Terms and Conditions")
        else:
            try:
                con=sqlite3.connect(database="RMS.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exits please try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password)Values(?,?,?,?,?,?,?)",
                    (self.txt_fname.get(),
                    self.txt_lname.get(),
                    self.txt_contact.get(),
                    self.txt_email.get(),
                    self.box_question.get(),
                    self.txt_answer.get(),
                    self.txt_password.get()
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register successfull",parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to  :{str(es)}",parent=self.root)
        
        
        

if __name__== "__main__":
    root = Tk()
    Object = register_class(root)
    root.mainloop()

