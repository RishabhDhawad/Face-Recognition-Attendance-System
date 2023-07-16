from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Pannel")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("Algerian",20,"bold"),bg="lightblue",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #first image
        img_top=Image.open(r"Images\n.jpg")
        img_top=img_top.resize((650, 700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)


        # second image
        img_bottom=Image.open(r"Images\re1.jpg")
        img_bottom = img_bottom.resize((950, 700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

        # Button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("Algerian",18,"bold"),bg="darkgreen",fg="yellow")
        b1_1.place(x=365,y=620,width=200,height=40)

        # Program for Face Recognition --------------------

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features= classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)   

        coord=[]
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h+20,x:x+w+20])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="khomdb")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student1 where id="+str(id))
                n = my_cursor.fetchone()

                n = str(n)
                print(n)
                # n="+".join(n)

                my_cursor.execute("select Roll from student1 where id="+str(id))
                r=my_cursor.fetchone()
                r = str(r)
                # r = "+".join(r)

                my_cursor.execute("select Dep from student1 where id="+str(id))
                d=my_cursor.fetchone()
                d = str(d)
                # d = "+".join(d)

                my_cursor.execute("select id from student1 where id="+str(id))
                i=my_cursor.fetchone()
                i = str(i)
                # i = "+".join(i)

                if confidence> 80:
                    cv2.putText(img,f"id: {i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                
                else:
                    cv2.rectangle(img,(x,y),(x+w+20,y+h+20),(0,0,255),3)
                    speak_va("Warning!!! Unknown Face")
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

        return coord 
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)   
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            # speak_va("Welcome to Face Recognition World")
            cv2.imshow("Welcome to face Recognition",img)


            if cv2.waitKey(1)==13:
                
                break
        video_cap.release()
        cv2.destroyAllWindows()

        # df_state=pd.read_csv(r"E:\6th sem\my_project\Face_reg\face_recognize_student_attendence_system\Teamkyzen23.csv")
        df_state = pd.read_csv(r"C:\Users\ACER\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Teamkyzen23.csv")
    
        # Dup_Rows = df_state[df_state.duplicated()]

        DF_RM_DUP = df_state.drop_duplicates(keep=False)



        DF_RM_DUP.to_csv('test1.csv', index=False)






if __name__ == "__main__":
    root=Tk()
    obj=Face_R
    ecognition(root)
    root.mainloop()