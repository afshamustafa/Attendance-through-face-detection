from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition system")
        
        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_ref=StringVar()
        self.var_Name=StringVar()
        self.var_Section=StringVar()
        self.var_Gender=StringVar()
        self.var_Email=StringVar()
        self.var_address=StringVar()
        self.var_Phone=StringVar()
        self.var_DOB=StringVar()
        self.var_CT=StringVar()
        
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
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=35)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=38,width=1480,height=500)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student details",font=("times new roman",20,"bold"))
        left_frame.place(x=10,y=5,width=720,height=480)
        
        #current course frame
        current_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course details",font=("times new roman",12,"bold"),bg="white",fg="blue")
        current_frame.place(x=10,y=20,width=700,height=100)
        
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=2,pady=2)
        
        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("times new roman",12,),width=20,state="readonly")
        dep_combo["values"]=("CSE","IT","Emerging Technologies","Computational Intelligence","Aeronautical","Mechanical","ECE","EEE")
        dep_combo.grid(row=0,column=1,padx=2,pady=2)
        
        co_label=Label(current_frame,text="Course",font=("times new roman",12,"bold"))
        co_label.grid(row=0,column=2,padx=2,pady=2)
        
        co_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font=("times new roman",12,),width=20)
        co_combo.grid(row=0,column=3,padx=2,pady=2)
        
        ye_label=Label(current_frame,text="Year",font=("times new roman",12,"bold"))
        ye_label.grid(row=1,column=0,padx=2,pady=2)
        
        ye_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,),width=20,state="readonly")
        ye_combo["values"]=("2020-2024","2021-2025","2022-2026","2023-2027")
        ye_combo.grid(row=1,column=1,padx=2,pady=2)
        
        sem_label=Label(current_frame,text="Semester",font=("times new roman",12,"bold"))
        sem_label.grid(row=1,column=2,padx=2,pady=2)
        
        sem_combo=ttk.Combobox(current_frame,textvariable=self.var_sem,font=("times new roman",12,),width=20,state="readonly")
        sem_combo["values"]=("Semester 1","Semester 2")
        sem_combo.grid(row=1,column=3,padx=2,pady=2)
        
        #student info frame
        info_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student information",font=("times new roman",12,"bold"),bg="white",fg="blue")
        info_frame.place(x=10,y=120,width=700,height=320)
        
        stid_label=Label(info_frame,text="Student ID",font=("times new roman",12,"bold"))
        stid_label.grid(row=0,column=0,padx=2,sticky=W)
        stid_entry=ttk.Entry(info_frame,textvariable=self.var_id,width=20,font=("times new roman",12))
        stid_entry.grid(row=0,column=1,padx=20,sticky=W)
        
        ref_label=Label(info_frame,text="Ref_no",font=("times new roman",12,"bold"))
        ref_label.grid(row=0,column=2,padx=2,sticky=W)
        ref_entry=ttk.Entry(info_frame,textvariable=self.var_ref,width=20,font=("times new roman",12))
        ref_entry.grid(row=0,column=3,padx=20,sticky=W)
        
        stnm_label=Label(info_frame,text="Name",font=("times new roman",12,"bold"))
        stnm_label.grid(row=1,column=0,padx=2,sticky=W)
        stnm_entry=ttk.Entry(info_frame,textvariable=self.var_Name,width=20,font=("times new roman",12))
        stnm_entry.grid(row=1,column=1,padx=20,sticky=W)
        
        stdiv_label=Label(info_frame,text="Section",font=("times new roman",12,"bold"))
        stdiv_label.grid(row=1,column=2,padx=2,pady=2,sticky=W)
        stdiv_entry=ttk.Entry(info_frame,textvariable=self.var_Section,width=20,font=("times new roman",12))
        stdiv_entry.grid(row=1,column=3,padx=20,pady=10,sticky=W)
        
        stgen_label=Label(info_frame,text="Gender",font=("times new roman",12,"bold"))
        stgen_label.grid(row=2,column=0,padx=2,pady=2,sticky=W)
        stgen_entry=ttk.Entry(info_frame,textvariable=self.var_Gender,width=20,font=("times new roman",12))
        stgen_entry.grid(row=2,column=1,padx=20,pady=10,sticky=W)
        
        stem_label=Label(info_frame,text="Email",font=("times new roman",12,"bold"))
        stem_label.grid(row=2,column=2,padx=2,pady=2,sticky=W)
        stem_entry=ttk.Entry(info_frame,textvariable=self.var_Email,width=20,font=("times new roman",12))
        stem_entry.grid(row=2,column=3,padx=20,pady=10,sticky=W)
        
        stadd_label=Label(info_frame,text="Address",font=("times new roman",12,"bold"))
        stadd_label.grid(row=3,column=0,padx=2,pady=2,sticky=W)
        stadd_entry=ttk.Entry(info_frame,textvariable=self.var_address,width=20,font=("times new roman",12))
        stadd_entry.grid(row=3,column=1,padx=20,pady=10,sticky=W)
        
        stph_label=Label(info_frame,text="Phone",font=("times new roman",12,"bold"))
        stph_label.grid(row=3,column=2,padx=2,pady=2,sticky=W)
        stph_entry=ttk.Entry(info_frame,textvariable=self.var_Phone,width=20,font=("times new roman",12))
        stph_entry.grid(row=3,column=3,padx=20,pady=10,sticky=W)
        
        stpph_label=Label(info_frame,text="DOB",font=("times new roman",12,"bold"))
        stpph_label.grid(row=4,column=0,padx=2,pady=2,sticky=W)
        stpph_entry=ttk.Entry(info_frame,textvariable=self.var_DOB,width=20,font=("times new roman",12))
        stpph_entry.grid(row=4,column=1,padx=20,pady=10,sticky=W)
        
        stt_label=Label(info_frame,text="Class Teacher",font=("times new roman",12,"bold"))
        stt_label.grid(row=4,column=2,padx=2,pady=2,sticky=W)
        stt_entry=ttk.Entry(info_frame,textvariable=self.var_CT,width=20,font=("times new roman",12))
        stt_entry.grid(row=4,column=3,padx=20,pady=10,sticky=W)
        
        #radio buttons
        self.var_rd1=StringVar()
        rdbtn1=ttk.Radiobutton(info_frame,variable=self.var_rd1,text="Take photo sample",value="Yes")
        rdbtn1.grid(row=7,column=1)
        
        self.var_rd2=StringVar()
        rdbtn2=ttk.Radiobutton(info_frame,variable=self.var_rd1,text="No photo sample",value="No")
        rdbtn2.grid(row=7,column=2)
        
        #radio buttons frame
        btn_frame=Frame(info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=230,width=695,height=30)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="White")
        save_btn.grid(row=0,column=0)
        
        up_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="White")
        up_btn.grid(row=0,column=1)
        
        del_btn=Button(btn_frame,text="Delete",command=self.del_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="White")
        del_btn.grid(row=0,column=2)
        
        re_btn=Button(btn_frame,text="Reset",command=self.res_data,width=18,font=("times new roman",12,"bold"),bg="blue",fg="White")
        re_btn.grid(row=0,column=3)
        
        btn_frame1=Frame(info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=260,width=695,height=30)
        
        take_btn=Button(btn_frame1,text="Take Photo",command=self.gen_data,width=38,font=("times new roman",12,"bold"),bg="blue",fg="White")
        take_btn.grid(row=0,column=0)
        
        upd_btn=Button(btn_frame1,text="Update Photo",command=self.gen_data,width=38,font=("times new roman",12,"bold"),bg="blue",fg="White")
        upd_btn.grid(row=0,column=1)
        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student details",font=("times new roman",20,"bold"))
        right_frame.place(x=740,y=5,width=720,height=480)
        
        #search system
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search system",font=("times new roman",12,"bold"),bg="white",fg="blue")
        search_frame.place(x=10,y=20,width=700,height=70)
        
        srch_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"))
        srch_label.grid(row=0,column=0,padx=2,pady=2,sticky=W)
        
        srch_combo=ttk.Combobox(search_frame,font=("times new roman",12,),width=15,state="readonly")
        srch_combo["values"]=("StudentID","Phone")
        srch_combo.grid(row=0,column=1,padx=2,pady=2)
        srch_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12))
        srch_entry.grid(row=0,column=2,padx=20,pady=10,sticky=W)
        
        srch_btn=Button(search_frame,text="Search",width=15,font=("times new roman",12,"bold"),bg="blue",fg="White")
        srch_btn.grid(row=0,column=3)
        
        all_btn=Button(search_frame,text="Show All",width=15,font=("times new roman",12,"bold"),bg="blue",fg="White")
        all_btn.grid(row=0,column=4)
        
        #table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=100,width=710,height=260)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.st_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","ref","Name","Section","Gender","Email","address","Phone","DOB","CT","Photo"))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.st_table.xview)
        scroll_y.config(command=self.st_table.yview)
        
        self.st_table.heading("dep",text="Department")
        self.st_table.heading("course",text="Course")
        self.st_table.heading("year",text="Year")
        self.st_table.heading("sem",text="Semester")
        self.st_table.heading("id",text="StudentID")
        self.st_table.heading("ref",text="ReferenceNo")
        self.st_table.heading("Name",text="Name")
        self.st_table.heading("Section",text="Section")
        self.st_table.heading("Gender",text="Gender")
        self.st_table.heading("Email",text="Email")
        self.st_table.heading("address",text="Address")
        self.st_table.heading("Phone",text="Phone")
        self.st_table.heading("DOB",text="DOB")
        self.st_table.heading("CT",text="Class teacher")
        self.st_table.heading("Photo",text="Photo sample status")
        self.st_table["show"]="headings"
        
        self.st_table.column("dep",width=100)
        self.st_table.column("course",width=100)
        self.st_table.column("year",width=100)
        self.st_table.column("sem",width=100)
        self.st_table.column("id",width=100)
        self.st_table.column("ref",width=100)
        self.st_table.column("Name",width=100)
        self.st_table.column("Section",width=100)
        self.st_table.column("Gender",width=100)
        self.st_table.column("Email",width=100)
        self.st_table.column("address",width=100)
        self.st_table.column("Phone",width=100)
        self.st_table.column("DOB",width=100)
        self.st_table.column("CT",width=100)
        self.st_table.column("Photo",width=150)
        
        self.st_table.pack(fill=BOTH,expand=1)
        self.st_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_dep.get()=="" or self.var_Name.get=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are mandatory")
        else:
           try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Afshaafsha@123",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_id.get(),
                                                                                        self.var_ref.get(),
                                                                                        self.var_Name.get(),
                                                                                        self.var_Section.get(),
                                                                                        self.var_Gender.get(),
                                                                                        self.var_Email.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_Phone.get(),
                                                                                        self.var_DOB.get(),
                                                                                        self.var_CT.get(),
                                                                                        self.var_rd1.get()
                                                                                        )) 

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student details has been added")
           except Exception as ex:
            messagebox.showerror("Error",f"Due To:{str(ex)}")
            
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Afshaafsha@123",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.st_table.delete(*self.st_table.get_children())
            for i in data:
                self.st_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_focus=self.st_table.focus()
        content=self.st_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_ref.set(data[5]),
        self.var_Name.set(data[6]),
        self.var_Section.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_Email.set(data[9]),
        self.var_address.set(data[10]),
        self.var_Phone.set(data[11]),
        self.var_DOB.set(data[12]),
        self.var_CT.set(data[13]),
        self.var_rd1.set(data[14])
        
    #update function
    def update_data(self):
        if self.var_dep.get()=="" or self.var_Name.get=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are mandatory")
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update?")
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Afshaafsha@123",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Ref=%s,Name=%s,Section=%s,Gender=%s,Email=%s,Address=%s,Phone=%s,DOB=%s,CT=%s,Photosample=%s where St_id=%s",(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                                self.var_ref.get(),
                                                                                                                                                                                                                self.var_Name.get(),
                                                                                                                                                                                                                self.var_Section.get(),
                                                                                                                                                                                                                self.var_Gender.get(),
                                                                                                                                                                                                                self.var_Email.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_Phone.get(),
                                                                                                                                                                                                                self.var_DOB.get(),
                                                                                                                                                                                                                self.var_CT.get(),
                                                                                                                                                                                                                self.var_rd1.get(),
                                                                                                                                                                                                                self.var_id.get()       
                                                                                                                                                                                               ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Updated!")
                conn.commit()
                self.fetch_data()
                conn.close() 
                
            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}")
                
    #delete function
    def del_data(self):
        if self.var_id.get()=="":
              messagebox.showerror("Error","ID mandatory")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Do you want to delete the data?")
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Afshaafsha@123",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where St_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not Delete:
                        return
                messagebox.showinfo("Success","Deleted!")
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}")
                
    #reset function
    def res_data(self):
        self.var_dep.set("")
        self.var_course.set("")
        self.var_year.set("")
        self.var_sem.set("")
        self.var_id.set("")
        self.var_ref.set("")
        self.var_Name.set("")
        self.var_Section.set("")
        self.var_Gender.set("")
        self.var_Email.set("")
        self.var_address.set("")
        self.var_Phone.set("")
        self.var_DOB.set("")
        self.var_CT.set("")
        self.var_rd1.set("")
        
    #take photo
    def gen_data(self):
        if ((self.var_dep.get()=="") or (self.var_Name.get=="") or (self.var_id.get()=="")):
            messagebox.showerror("Error","All fields are mandatory")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Afshaafsha@123",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                ref=0
                for x in myresult:
                    ref+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,St_id=%s,Name=%s,Section=%s,Gender=%s,Email=%s,Address=%s,Phone=%s,DOB=%s,CT=%s,Photosample=%s where Ref=%s",(
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                                            self.var_id.get(),
                                                                                                                                                                                                            self.var_Name.get(),
                                                                                                                                                                                                            self.var_Section.get(),
                                                                                                                                                                                                            self.var_Gender.get(),
                                                                                                                                                                                                            self.var_Email.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_Phone.get(),
                                                                                                                                                                                                            self.var_DOB.get(),
                                                                                                                                                                                                            self.var_CT.get(),
                                                                                                                                                                                                            self.var_rd1.get(),
                                                                                                                                                                                                            self.var_ref.get()    
                                                                                                                                                                                               ))
                conn.commit()
                self.fetch_data()
                self.res_data()
                conn.close()
                
    #load face frontals
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3, minimum neughbour=5
                    
                    for (x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_crop(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_crop(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/user."+str(ref)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Completed generation of data set")
            except Exception as ex:
                messagebox.showerror("Error",f"Due To:{str(ex)}") 
                
                
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()