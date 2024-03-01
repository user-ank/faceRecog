from tkinter import*
from tkinter import ttk
# powerful GUI application software
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Attandance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

           # first image
        img = Image.open(r"project_images/student.jpeg")
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # second image
        img1 = Image.open(r"project_images/image 2.jpeg")
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

         # bg image
        img3 = Image.open(
            r"project_images/7100be04-c18c-4b33-ae41-7b4ef2cadadf.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_lbl = Label(self.root, image=self.photoimg3)
        bg_lbl.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_lbl, text="ATTENDANCE MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_lbl, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)


        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(
            r"project_images/IMG_20230308_114906.jpeg")
        img_left = img_left.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=300)

        # Lables and Entry

        # attendance id
        attendanceId_label = Label(left_inside_frame, text="AttendanceId:", font=(
            "times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, sticky=W)


        # Right lable frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=740, y=10, width=690, height=580)

if __name__ == "__main__":
    root = Tk()
    obj = Attandance(root)
    root.mainloop()
