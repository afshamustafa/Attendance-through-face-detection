from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Training Data system")
        
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
        title_lbl=Label(bg_img,text="TRAINING DATA SET",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=35)
        
        #button
        b1_1=Button(bg_img,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="blue",fg="white")
        b1_1.place(x=0,y=60,width=1500,height=40)
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert("L")   #gray scale image
            imgnp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split(".")[1])
        
            faces.append(imgnp)
            ids.append(id)
            cv2.imshow("Training",imgnp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Training data set completed!")
        
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()