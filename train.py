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
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Pannel")


        title_lb1 = Label(self.root,text="Train Data Set",font=("verdana",30,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Image which will be on top
        img_top=Image.open("face_recognize_student_attendence_system\Images\developer.png")         
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=55,width=1530,height=325)

        # Creating Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Algerian",25,"bold"),bg="green",fg="white")
        b1_1.place(x=500,y=450,width=300,height=150)

        # Image which will be on Bottom of the page..
        img_bottom=Image.open("face_recognize_student_attendence_system\Images\developer.png")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)  #Antialias lea high level image lai low level mah convert garxa
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir = ("data")
        path=[os.path.join(data_dir,file) for  file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # Gray Scale Image
            imageNp=np.array(img,'uint8') # unont8 is a datatype here
            id=int(os.path.split(image)[1].split('.')[1]) 

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the Classifier and Saving
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        speak_va("Training datasets completed successfully!")
        messagebox.showinfo("Result","Training datasets completed successfully!",parent=self.root)
        # self.root.destroy()

        







if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()