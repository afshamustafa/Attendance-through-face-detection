from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Detect:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detection")
        
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
        title_lbl=Label(bg_img,text="FACE DETECTION",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=35)
        
         #button
        b1_1=Button(bg_img,text="DETECT & RECOGNIZE",command=self.face_recognise,cursor="hand2",font=("times new roman",20,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=100,width=500,height=40)
        
        #attendance
    def mark_attendance(self,s,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myData=f.readlines()
            name_list=[]
            for line in myData:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((n not in name_list) and (d not in name_list) and (s not in name_list) and (r not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dt=now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{r},{n},{d},{dt},{d1},Present")
        
        #face recognition
    def face_recognise(self):
        def draw_boundary(img,classifier,scale,min,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scale,min)
            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Afshaafsha@123",database="face_recognition")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where Ref="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Dep from student where Ref="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                my_cursor.execute("select St_id from student where Ref="+str(id))
                s=my_cursor.fetchone()
                s="+".join(s)
                
                my_cursor.execute("select Ref from student where Ref="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                
                if confidence>77:
                    cv2.putText(img,f"Ref:{r}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"ID:{s}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(s,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,y]
            return coord
        def recognise(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognise(img,clf,faceCascade)
            cv2.imshow("Face recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
           
            
        
if __name__=="__main__":
    root=Tk()
    obj=Detect(root)
    root.mainloop()