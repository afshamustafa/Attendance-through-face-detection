
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from recognize import Detect
from attendance import Attendance

class Face_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition system")
        #logo
        img=Image.open(r"C:\Users\hi\OneDrive\Desktop\Face_recognition_system\logo.jpg")
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=500,y=0,width=500,height=240)
        #bg
        img1=Image.open(r"C:\Users\hi\OneDrive\Desktop\Face_recognition_system\bg.jpg")
        img1=img1.resize((1530,790),Image.Resampling.BOX)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=240,width=1500,height=550)
        title_lbl=Label(bg_img,text="ATTENDANCE THROUGH FACE DETECTION",font=("times new roman",40,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #student button
        img2=Image.open(r"C:\Users\hi\OneDrive\Desktop\Face_recognition_system\st info.jpg")
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        b1=Button(bg_img,image=self.photoimg2,command=self.Stud_details,cursor="hand2")
        b1.place(x=70,y=100,width=200,height=200)
        
        b1_1=Button(bg_img,text="Student Details",command=self.Stud_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=70,y=300,width=200,height=40)
        
        #detect face button
        img3=Image.open(r"C:\Users\hi\OneDrive\Desktop\Face_recognition_system\face-recognition.jpg")
        img3=img3.resize((200,200),Image.Resampling.BOX)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b2=Button(bg_img,image=self.photoimg3,cursor="hand2")
        b2.place(x=450,y=100,width=200,height=200)
        
        b2_1=Button(bg_img,text="Face Detection",command=self.detect_class,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b2_1.place(x=450,y=300,width=200,height=40)
        
        #Train data button
        img4=Image.open(r"C:\Users\hi\OneDrive\Desktop\Face_recognition_system\train.png")
        img4=img4.resize((200,200),Image.Resampling.BOX)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b3=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b3.place(x=850,y=100,width=200,height=200)
        
        b3_1=Button(bg_img,text="Train data",command=self.train_class,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b3_1.place(x=850,y=300,width=200,height=40)
        
        #attendance button
        img6=Image.open(r"C:\Users\hi\OneDrive\Desktop\Face_recognition_system\attendance.jpg")
        img6=img6.resize((200,200),Image.Resampling.BOX)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b5=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b5.place(x=1250,y=100,width=200,height=200)
        
        b5_1=Button(bg_img,text="Attendance",command=self.att_class,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b5_1.place(x=1250,y=300,width=200,height=40)
        
    def Stud_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_class(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def detect_class(self):
        self.new_window=Toplevel(self.root)
        self.app=Detect(self.new_window)
    def att_class(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)   
    
        
if __name__=="__main__":
    root=Tk()
    obj=Face_system(root)
    root.mainloop()