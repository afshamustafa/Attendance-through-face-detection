from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
mydata=[]

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition system")
        
        #variables
        self.var_attid=StringVar()
        self.var_ref=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_attst=StringVar()
        
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
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=35)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=38,width=1480,height=500)
        
         #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance details",font=("times new roman",20,"bold"))
        left_frame.place(x=10,y=5,width=720,height=480)
        
        l_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        l_inside_frame.place(x=10,y=20,width=700,height=500)
        
        #label entry
        attid_label=Label(l_inside_frame,text="Attendance ID",font=("times new roman",12,"bold"))
        attid_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)
        attid_entry=ttk.Entry(l_inside_frame,width=20,textvariable=self.var_attid,font=("times new roman",12))
        attid_entry.grid(row=0,column=1,padx=20,pady=5,sticky=W)
        
        ref_label=Label(l_inside_frame,text="Reference ID",font=("times new roman",12,"bold"))
        ref_label.grid(row=0,column=2,padx=2,pady=5,sticky=W)
        ref_entry=ttk.Entry(l_inside_frame,width=20,textvariable=self.var_ref,font=("times new roman",12))
        ref_entry.grid(row=0,column=3,padx=20,pady=5,sticky=W)
        
        nm_label=Label(l_inside_frame,text="Name",font=("times new roman",12,"bold"))
        nm_label.grid(row=1,column=0,padx=2,pady=5,sticky=W)
        nm_entry=ttk.Entry(l_inside_frame,width=20,textvariable=self.var_name,font=("times new roman",12))
        nm_entry.grid(row=1,column=1,padx=20,pady=5,sticky=W)
        
        dep_label=Label(l_inside_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=1,column=2,padx=2,pady=5,sticky=W)
        dep_entry=ttk.Entry(l_inside_frame,width=20,textvariable=self.var_dep,font=("times new roman",12))
        dep_entry.grid(row=1,column=3,padx=20,pady=5,sticky=W)
        
        dt_label=Label(l_inside_frame,text="Date",font=("times new roman",12,"bold"))
        dt_label.grid(row=2,column=0,padx=2,pady=5,sticky=W)
        dt_entry=ttk.Entry(l_inside_frame,width=20,textvariable=self.var_date,font=("times new roman",12))
        dt_entry.grid(row=2,column=1,padx=20,pady=5,sticky=W)
        
        tm_label=Label(l_inside_frame,text="Time",font=("times new roman",12,"bold"))
        tm_label.grid(row=2,column=2,padx=2,pady=5,sticky=W)
        tm_entry=ttk.Entry(l_inside_frame,width=20,textvariable=self.var_time,font=("times new roman",12))
        tm_entry.grid(row=2,column=3,padx=20,pady=5,sticky=W)
        
        attst_label=Label(l_inside_frame,text="Attendance status",font=("times new roman",12,"bold"))
        attst_label.grid(row=3,column=0,padx=2,pady=5,sticky=W)
        attst_entry=ttk.Entry(l_inside_frame,width=20,textvariable=self.var_attst,font=("times new roman",12))
        attst_entry.grid(row=3,column=1,padx=20,pady=5,sticky=W)
        
        #radio buttons frame
        btn_frame=Frame(l_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=695,height=30)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importcsv,width=18,font=("times new roman",12,"bold"),bg="blue",fg="White")
        save_btn.grid(row=0,column=0)
        
        up_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,width=18,font=("times new roman",12,"bold"),bg="blue",fg="White")
        up_btn.grid(row=0,column=1)
        
        del_btn=Button(btn_frame,text="Delete",width=18,font=("times new roman",12,"bold"),bg="blue",fg="White")
        del_btn.grid(row=0,column=2)
        
        re_btn=Button(btn_frame,text="Reset",command=self.reset,width=18,font=("times new roman",12,"bold"),bg="blue",fg="White")
        re_btn.grid(row=0,column=3)
        
         #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance",font=("times new roman",20,"bold"))
        right_frame.place(x=740,y=5,width=720,height=480)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=705,height=490)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceTable=ttk.Treeview(table_frame,column=("id","ref","Name","Department","Date","Time","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceTable.xview)
        scroll_y.config(command=self.AttendanceTable.yview)
        
        self.AttendanceTable.heading("id",text="Attendance ID")
        self.AttendanceTable.heading("ref",text="Referance ID")
        self.AttendanceTable.heading("Name",text="Name")
        self.AttendanceTable.heading("Department",text="Department")
        self.AttendanceTable.heading("Date",text="Date")
        self.AttendanceTable.heading("Time",text="Time")
        self.AttendanceTable.heading("Status",text="Attendance Status")
        
        self.AttendanceTable["show"]="headings"
        
        self.AttendanceTable.pack(fill=BOTH,expand=1)
        self.AttendanceTable.bind("<ButtonRelease>",self.get_cursor)
        
    #fetch data
    def fetchData(self,rows):
        self.AttendanceTable.delete(*self.AttendanceTable.get_children())
        for i in rows:
            self.AttendanceTable.insert("",END,values=i)
        
    def importcsv(self):
       global mydata
       mydata.clear()
       fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
       with open(fln) as myfile:
           csvread=csv.reader(myfile,delimiter=",")
           for i in csvread:
               mydata.append(i)
           self.fetchData(mydata)
    
    #export
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)     
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Data has exported to"+os.path.basename(fln)+"successfully")
        except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceTable.focus()
        content=self.AttendanceTable.item(cursor_row)
        row=content["values"]
        self.var_attid.set(row[0]) 
        self.var_ref.set(row[1])
        self.var_name.set(row[2])
        self.var_dep.set(row[3])
        self.var_date.set(row[4])
        self.var_time.set(row[5])
        self.var_attst.set(row[6])
    def reset(self):
        self.var_attid.set("") 
        self.var_ref.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_attst.set("")  
        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()