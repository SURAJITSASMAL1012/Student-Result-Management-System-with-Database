from tkinter import *
from PIL import Image,ImageDraw,ImageTk
from datetime import*
import time
from math import*
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import os
class LogIn:
    def __init__(self,root):
        self.root=root
        self.root.title("LOG IN System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        #title=Label(self.root,text="Analog Clock | By Surajit",font=("times new roman",30,"bold"),bg="#04444a",fg="white").place(x=0,y=0,relwidth=1)
        #🕐🕐🕐Background colors for the clock🕐🕐🕐
        left_label=Label(self.root,bg="#08A3D2",bd=0)
        left_label.place(x=0,y=0,relheight=1,width=600)

        right_label=Label(self.root,bg="#08A3D2",bd=0)# #031F3C
        right_label.place(x=0,y=0,relheight=1,relwidth=1)
        #⭐⭐Frames⭐⭐
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=790,height=500)

        title=Label(login_frame,text="LOGIN HERE ",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        email=Label(login_frame,text="EMAIL ADDRESS ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.text_email=Entry(login_frame,font=("times new roman",17,"bold"),bg="lightgray")
        self.text_email.place(x=250,y=180,width=350)

        password=Label(login_frame,text="PASSWORD ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.text_password=Entry(login_frame,font=("times new roman",17,"bold"),bg="lightgray")
        self.text_password.place(x=250,y=280,width=350)

        button_register=Button(login_frame,text=("Register a new Account?"),font=("times new roman",12,"bold"),bg="gray",cursor="hand2",command=self.register_window).place(x=250,y=320)
        button_forgetp=Button(login_frame,text=("Forget Password"),font=("times new roman",12,"bold"),bg="white",fg="red",cursor="hand2",command=self.forget_password).place(x=450,y=320)
        
        button_login=Button(login_frame,text=("LOGIN"),font=("times new roman",18,"bold"),fg="white",bg="#B00857",cursor="hand2",command=self.login).place(x=250,y=375,height=40,width=180)

        #🕐🕐🕐🕐🕐🕐🕐🕐Clock
        self.lbl=Label(self.root,text="Devoloped By Surajit",font=("Book Antiqua",18,"bold"),compound=BOTTOM,bg="#081923",fg="white",bd=0,relief=RAISED)
        self.lbl.place(x=90,y=120,height=450,width=350)
        #self.clock_img()
        self.working()
    def reset_password(self):
        if self.box_question.get()=="Select" or self.text_answer.get()=="" or self.text_new_passw.get()=="":
            messagebox.showerror("Error","All Fields are required ",parent=self.root1)
        else:
            try:
                con=sqlite3.connect(database="RMS.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.text_email.get(),self.box_question.get(),self.text_answer.get(),))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Please Select a Correct Secuirity Question / Answer",parent=self.root1)
                else:
                    cur.execute("update employee set password=? where email=?",(self.text_new_passw.get(),self.text_email.get(),))
                    #row1=cur.fetchone()
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been successfully changed,Please LogIn with new Password",parent=self.root1)
                    self.root1.destroy()
                    self.clear()
            except Exception as ex:
                messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root1)
    def clear(self):
        self.box_question.current(0)
        self.text_new_passw.set("")
        self.text_answer.set("")
        self.text_password.set("")
        self.text_email.set("")
    def forget_password(self):
        if self.text_email.get()=="":
            messagebox.showerror("Error","Please Enter a  email to reset your password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="RMS.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.text_email.get(),))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Please Enter a valid email to reset your password",parent=self.root)
                    #messagebox.showerror("Error","Invalid UserName & Password ...try again",parent=self.root)
                else:
                    con.close()
                    self.root1=Toplevel()
                    self.root1.title("Forget Password")
                    self.root1.geometry("350x400+550+150")
                    self.root1.focus_force()
                    self.root1.grab_set()
                    self.root1.config(bg="white")
                    t=Label(self.root1,text=("Forget Password"),font=("times new roman",18,"bold"),bg="white",fg="red").place(x=1,y=10,relwidth=1)
                    #©️©️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️Forget Password ©️©️
                    question=Label(self.root1,text="Security Question ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=40,y=100)
                    self.box_question=ttk.Combobox(self.root1,font=("times new roman",15),state='readonly',justify=CENTER)
                    self.box_question['values']=("Select","Your Birth Place","Your Best Friend Name","Your Favorite fruit")
                    self.box_question.place(x=40,y=130,width=250)
                    self.box_question.current(0)
                    answer=Label(self.root1,text="Answer ",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=40,y=180)
                    self.text_answer=Entry(self.root1,font=("times new roman",15),bg="lightgray")
                    self.text_answer.place(x=40,y=210,width=250)
                    new_password=Label(self.root1,text="New Password",font=("times new roman",17,"bold"),bg="white",fg="gray").place(x=40,y=260)
                    self.text_new_passw=Entry(self.root1,font=("times new roman",15),bg="lightgray")
                    self.text_new_passw.place(x=40,y=290,width=250)

                    button_change_password=Button(self.root1,text="Reset Password",bg="green",fg="white",font=("times new roman",15,"bold"),cursor="hand2",command=self.reset_password).place(x=80,y=340)
                
            except Exception as ex:
                messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root1)
    
        
        

    def register_window(self):
        self.root.destroy()
        #import register
        os.system("python register.py")

    def login(self):
        if self.text_email.get()=="" or self.text_password.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="RMS.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=? ",(self.text_email.get(),self.text_password.get(),))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Invalid UserName & Password ...try again",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome...{self.text_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python Dashboard.py")
                con.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Error Due to : {str(ex)}",parent=self.root)
    
    def clock_img(self,hr, min_ , sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        bg=Image.open("c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        #🕐🕐Formula For roatate the Clock🕐🕐
        '''angle_radians = angle_degrees * math.pi / 180
        line_length=100
        center_x=250
        center_y=250
        end_x=center_x + line_length *math.cos(angle_radians)
        end_y=center_y - line_length * math.sin(angle_radians)'''
        #Hour Line🐤🐤🐤🕐🕐🕐
        #  x,y,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        
        #Minute Line🕐🕐🕐🕐
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)

        #Second Line 🕐🕐🕐🕐🕐
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=2)

        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("clock_new.png")

    def working(self):
        h=datetime.now().hour
        m=datetime.now().minute
        s=datetime.now().second
        hr = (h/12)*360
        min_ =(m/60)*360
        sec_ =(s/60)*360
        self.clock_img(hr, min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

root=Tk()
object=LogIn(root)
root.mainloop()
