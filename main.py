from tkinter import *
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
import  os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x700+0+0")
        self.root.title("Smart Attendance System")
        
        img = Image.open("Images_GUI/facialrecognition.png")
        img = img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lb1 = Label(self.root, image = self.photoimg)
        f_lb1.place(x = 0, y = 0, width = 1366, height = 130)
        
        bg1=Image.open("Images_GUI/bg2.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)
        
        title_lb1 = Label(bg_img,text="Attendance Managment System Using Facial Recognition",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open("Images_GUI/std1.jpg")
        std_img_btn=std_img_btn.resize((240,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_details,image=self.std_img1,cursor="hand2")
        std_b1.place(x=200,y=100,width=240,height=180)
        
        std_b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("tahoma",20,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=200,y=280,width=240,height=45)
        
        # Detect Face  button 2
        det_img_btn=Image.open("Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((240,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_recognition,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=550,y=200,width=240,height=180)

        det_b1_1 = Button(bg_img,text="Face Detector",command=self.face_recognition,cursor="hand2",font=("tahoma",20,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=550,y=380,width=240,height=45)
                
         # Train   button 3
        tra_img_btn=Image.open("Images_GUI/tra1.jpg")
        tra_img_btn=tra_img_btn.resize((240,180),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_dataset,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=200,y=330,width=240,height=180)

        tra_b1_1 = Button(bg_img,text="Data Train",command=self.train_dataset,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=200,y=510,width=240,height=45)
        
        # Photo   button 4
        pho_img_btn=Image.open("Images_GUI/photos.png")
        pho_img_btn=pho_img_btn.resize((240,180),Image.ANTIALIAS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_folder,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=900,y=100,width=240,height=180)

        pho_b1_1 = Button(bg_img,command=self.open_folder,text="Photos",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=900,y=280,width=240,height=45)
        
        # exit   button 5
        exi_img_btn=Image.open("Images_GUI/exi.jpg")
        exi_img_btn=exi_img_btn.resize((240,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=900,y=330,width=240,height=180)

        exi_b1_1 = Button(bg_img,text="Exit",command=self.close,cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=900,y=510,width=240,height=45)

        # ==================Functions Buttons=====================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_dataset(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def close(self):
        root.destroy()
        
    def open_folder(self):
        os.startfile("data_img")
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    