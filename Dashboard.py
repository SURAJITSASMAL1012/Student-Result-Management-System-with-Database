from email import message
from tkinter import*
from PIL import Image,ImageTk,ImageDraw#pip install pillow
from course import Course_Class
from student import Student_Class
from result import result_class
from report import report_class
from tkinter import messagebox
import os
from datetime import*
import time
from math import*
import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System ")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="white")
        #⭐icons⭐
        self.logo_dash=ImageTk.PhotoImage(file="logo.png")
        #1️⃣1️⃣1️⃣
        title=Label(self.root,text="Students Result Management System",compound=LEFT,padx=5,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
    
        #==Menu==
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",10),bg="white")
        M_Frame.place(x=10,y=75,width=1350,height=80)
        button_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2", command=self.add_course).place(x=20,y=5,width=200,height=40)
        button_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        button_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        button_view=Button(M_Frame,text="View",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        button_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        button_Exit=Button(M_Frame,text="Exit",font=( "goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_window).place(x=1120,y=5,width=200,height=40)

        #⭐Contents Window1️⃣🔢
        self.bg_image=Image.open("bg_2.png")
        self.bg_image=self.bg_image.resize((930,360),Image.ANTIALIAS)
        self.bg_image=ImageTk.PhotoImage(self.bg_image)
        self.lbl_image=Label(self.root,image=self.bg_image).place(x=400,y=180,width=930,height=360)

        #1️⃣Update Details..

        self.lbl_course=Label(self.root,text=" Tota Courses\n[ 0 ]",font=("goudy old style",20),bd=12,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text=" Tota Student\n[ 0 ]",font=("goudy old style",20),bd=12,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text=" Tota Results\n[ 0 ]",font=("goudy old style",20),bd=12,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)
        
        #🕐🕐🕐🕐Clock🕐🕐🕐🕐
        self.lbl=Label(self.root,text="Devoloped By Surajit",font=("Book Antiqua",18,"bold"),compound=BOTTOM,bg="#081923",fg="white",bd=0,relief=RAISED)
        self.lbl.place(x=10,y=180,height=450,width=350)
        #self.clock_img()
        self.working()
        
        #🐤Footer
        footer=Label(self.root,text="SRMS-Students Result Management system\nContact us for any Technical Issue : 97348xxx51\nMail us :surajitsasmal5041@gmail.com",font=("goudy old style",11),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_board_details()
##💖💖💖All the Function Connection with DashBoard to another file💖💖💖
    def update_board_details(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            cur.execute("Select * From course ")
            rc=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(rc))}]")

            cur.execute("Select * From student ")
            rc=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(rc))}]")

            cur.execute("Select * From result")
            rc=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(rc))}]")

            self.lbl_course.after(200,self.update_board_details)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
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

    def add_student(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=Student_Class(self.new_window)
    def add_course(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=Course_Class(self.new_window)   
    def add_result(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=result_class(self.new_window) 
    def add_report(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=report_class(self.new_window) 
    def logout(self):
        op=messagebox.askyesno("Confirm","Do You want to really Log Out?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python LogIn.py")
    def exit_window(self):
        op=messagebox.askyesno("Confirm","Do You want to really Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
            #os.system("python LogIn.py")
    

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
